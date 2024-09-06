from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = math.fmean(numbers)
    deviation = sum(math.fabs(x - mean) for x in numbers)
    return deviation / len(numbers)