import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from util import get_data


def clean_data(train_x: pd.DataFrame) -> pd.DataFrame:
    return train_x


def basic_model(train_x: pd.DataFrame, train_y: pd.Series, 
                test_x: pd.DataFrame, test_y: pd.Series, 
                show_fig: bool = True) -> float:
    
    if show_fig:        # placeholder
        plt.scatter([], [])
        plt.show()

    return float("inf")


def improve_model(train_x: pd.DataFrame, train_y: pd.Series, 
                  test_x: pd.DataFrame, test_y: pd.Series, 
                  MAE_basic: float) -> tuple[float, pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
    return float("inf"), pd.DataFrame(), pd.Series(), pd.DataFrame(), pd.Series()


def regularized_model(train_x: pd.DataFrame, train_y: pd.Series, 
                      test_x: pd.DataFrame, test_y: pd.Series) -> None:
    pass



def main() -> None:
    # cities:
    # Ljubljana, Montelimar, Dusseldorf, Budapest, Kassel, Oslo, Maastricht, 
    # Perpignan, Roma, Dresden, Heathrow, Tours, De_bilt, Stockholm, 
    # Muenchen, Sonnblick, Basel, Malmo]

    city, train_x, train_y, test_x, test_y = get_data()     # get_data(forced_city = "Malmo")

    print(f"You're working with data from {city}.")

    #### TASK 1 ####
    train_x = clean_data(train_x)

    #### TASK 2 ####
    MAE_basic: float = basic_model(train_x, train_y, test_x, test_y, show_fig=True)

    print(f"MAE of basic model is {MAE_basic}.")

    #### TASK 3 ####
    MAE_improved, train_x_adj, train_y_adj, test_x_adj, test_y_adj = improve_model(
        train_x, train_y, test_x, test_y, MAE_basic=MAE_basic
    )

    print(f"MAE of improved model is {MAE_improved}.")

    #### TASK 4 ####
    regularized_model(train_x_adj, train_y_adj, test_x_adj, test_y_adj)


if __name__ == "__main__":
    main()