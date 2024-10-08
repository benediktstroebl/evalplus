from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    return math.mean(abs(num - math.mean(numbers)) for num in numbers)