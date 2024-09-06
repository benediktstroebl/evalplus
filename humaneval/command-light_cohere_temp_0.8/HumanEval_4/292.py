Here is a Python script that contains a self-contained function that solves the given problem:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation
    """
    mean = sum(numbers) / len(numbers)
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mad
```
This function takes a list of numbers as an argument and returns the Mean Absolute Deviation. The MAD is calculated by finding the average of each element in the list, then finding the average of the squared differences between each element and the mean.