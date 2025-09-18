import random
from typing import Literal, Optional
import numpy as np
import pandas as pd

City = Literal[
    "Ljubljana", "Montelimar", "Dusseldorf", "Budapest", "Kassel", "Oslo", "Maastricht", 
    "Perpignan", "Roma", "Dresden", "Heathrow", "Tours", "De_bilt", "Stockholm", 
    "Muenchen", "Sonnblick", "Basel", "Malmo"
    ]

def get_data(
        path: str = "data/weather.csv", nsample: int = 400, forced_city: Optional[City] = None
        ) -> tuple[str, pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
    weather_all: pd.DataFrame = pd.read_csv(path, na_values="NA")

    city: str
    if forced_city:
        city = forced_city.lower().capitalize()
    else:
        city = random.choice(list(set(weather_all["city"])))

    weather_city: pd.DataFrame = weather_all[weather_all["city"] == city].dropna(
            axis=1
        ).drop(
            columns="city"
        ).reset_index(
            drop=True
        )
    
    test_df: pd.DataFrame = weather_city.sample(n=nsample)
    train_df: pd.DataFrame = weather_city.drop(test_df.index).reset_index(drop=True)
    test_df.reset_index(drop=True, inplace=True)

    return (
        city, 
        introduce_mess(train_df.drop(columns="temp_mean_next_day")), train_df["temp_mean_next_day"],
        test_df.drop(columns="temp_mean_next_day"), test_df["temp_mean_next_day"],
        )


def introduce_mess(data: pd.DataFrame) -> pd.DataFrame:
    # different wind speed units
    if "wind_speed" in data.columns and random.random() < 0.2:
        data["wind_speed"] = data["wind_speed"].map(
            lambda x: str(x) + "m/s" if random.random() < 0.5 else str(round(x * 3.6, 2)) + "km/h"
        )

    # int to str
    for col in data.columns:
        if random.random() < 0.2:
            data[col] = data[col].astype(str)

    # missing values
    for col in data.columns:
        data.loc[data.sample(frac=0.005).index, col] = np.nan
    
    # shuffle index
    if random.random() < 0.2:
        data = data.sample(frac=1)
    
    # irrelevant column
    if random.random() < 0.2:
        data[random.choice(["recorded_by", "author", "responsible_person"])] = random.choices(
            ["Marvin", "R2-D2", "T-800", "TARS", "Wall-E", "J.A.R.V.I.S."],
            k=len(data))

    return data


def main() -> None:
    pass
    
    
if __name__ == "__main__":
    main()
