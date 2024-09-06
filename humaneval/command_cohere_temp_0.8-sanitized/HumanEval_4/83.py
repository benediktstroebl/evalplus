import random
import numpy as np
import pytest
from typing import List
def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(numbers - np.mean(numbers)))