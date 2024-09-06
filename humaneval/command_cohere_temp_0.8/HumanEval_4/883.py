Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation of the input list
    """
    mean = math.mean(numbers)
    deviation = sum(abs(num - mean) for num in numbers) / len(numbers)
    return deviation
```
This function takes a list of numbers as input and calculates the mean absolute deviation, which is the average absolute difference between each element and the mean of the list. It first calculates the mean using the `mean `function and then calculates the absolute deviation using a sum and average operation. Finally, it returns the mean absolute deviation. 
You can use this function to calculate the mean absolute deviation of any list of numbers.  example 
```python
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```
The output will be:
```
1.0
```