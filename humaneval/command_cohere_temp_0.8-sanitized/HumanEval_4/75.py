from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    return math.sqrt(sum((x - num_mean) ** 2 for x, num_mean in zip(numbers, numbers)))