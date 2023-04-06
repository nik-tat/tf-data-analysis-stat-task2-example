import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    z = (x ** 2).sum()
    first = chi2.ppf((p + 1.0) / 2.0, 2 * x.shape[0])
    second = chi2.ppf((1.0 - p) / 2.0, 2 * x.shape[0])
    return (z / 45.0 / first) ** (1/2), (z / 45.0 / second) ** (1/2)
