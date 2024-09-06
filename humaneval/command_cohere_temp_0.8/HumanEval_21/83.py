Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list where the smallest number is 0 and the largest number is 1. This is achieved by calculating the fractional difference between each element and the smallest element, then multiplying this difference by the fractional difference between the largest element and the smallest element, and finally multiplying by 1 to avoid shrinking the largest element below 1. The approach ensures that the elements of the transformed list reflect their relative proportions to each other in the original list.