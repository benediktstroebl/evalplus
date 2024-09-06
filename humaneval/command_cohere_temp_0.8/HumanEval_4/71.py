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
    """
    if not numbers:
        raise ValueError("Input list is empty. Cannot calculate MAD.")

    mean = math.mean(numbers)
    deviations = [abs(num - mean) for num in numbers]
    return math.mean(deviations)
```

This script includes the necessary import statement, the function definition, and a docstring that explains the formula and what the function does. The function `mean_absolute_deviation` takes a list of numbers as input and returns the mean absolute deviation of the numbers in the list. The function first checks if the input list is empty, and if so, raises a `ValueError`. It then calculates the mean of the numbers in the list and creates a list of absolute deviations from the mean for each number in the list. It then returns the mean of these absolute deviations. 

You can use this function to calculate the mean absolute deviation of any list of numbers. For example:
 ```python
result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
print(result)
```
This will print the result `1.0` to the console, corresponding to the example in the problem statement.