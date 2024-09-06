from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    return math.sqrt(sum((x-mean(numbers))**2 for x in numbers)/len(numbers))
mean = lambda list1: sum(list1)/len(list1)