from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    devations = [abs(x - mean) for x in numbers]
    return math.fsum(devations) / len(devations)