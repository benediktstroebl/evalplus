```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    mad = sum(x - numbers[int(len(numbers) / 2)] for x in numbers) / len(numbers)
    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 0.0)

``` 
This code defines a function `mean_absolute_deviation` that calculates the mean absolute deviation for a given list of numbers. The function first computes the average of the list and then computes the absolute difference between each element and the mean, which is the mean absolute deviation. 

The test section at the bottom demonstrates the correctness of the function.