from typing import List
import numpy as np
import pytest
def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
numbers = [1.0, 2.0, 3.0, 4.0]