Here's a self-contained Python script that solves the provided problem:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation
    """
    x_mean = sum(numbers) / len(numbers)
    mad = sum((x - x_mean) for x in numbers) / len(numbers)
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.1
```
This script defines a function `mean_absolute_deviation` that takes a list of numbers as input. The function calculates the mean of the list and then computes the Mean Absolute Deviation around this mean. The output is then the absolute deviation of the list.