from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    dev = sum(abs(x - mean) for x in numbers) / len(numbers)
    return abs(dev)