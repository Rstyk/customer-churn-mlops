
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def prepare_features(df: pd.DataFrame, target_column: str = "Churn"):
    df = df.copy()
    y = df[target_column]
    X = df.drop(columns=[target_column])

    y = y.astype("string").str.strip().str.lower()
    y = y.map({"no": 0, "yes": 1})

    X = pd.get_dummies(X, drop_first=True)
    X = X.fillna(0)

    return X, y.astype(int)
