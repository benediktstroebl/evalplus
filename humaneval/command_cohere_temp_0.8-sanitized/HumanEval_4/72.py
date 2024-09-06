from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    return math.fabs(math.mean(numbers) - mean_absolute_deviation_helper(numbers)) / len(numbers)
def mean_absolute_deviation_helper(numbers: List[float]) -> float:
    return math.mean(math.fabs(num - math.mean(numbers)) for num in numbers)