from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    return math.mean(abs(x - statistics.mean(numbers) for x in numbers))