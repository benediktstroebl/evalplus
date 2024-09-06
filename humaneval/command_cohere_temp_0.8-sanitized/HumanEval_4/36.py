from typing import List
import numpy as np
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    return math.fabs(np.mean(numbers) - np.median(numbers))