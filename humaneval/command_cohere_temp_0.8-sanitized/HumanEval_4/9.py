from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    return math.sqrt(sum((x - sum(numbers)/len(numbers))**2 for x in numbers))