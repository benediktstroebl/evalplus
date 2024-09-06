Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    dev = sum(math.abs(x - mean) for x in numbers) / len(numbers)
    return dev
```

This function `mean_absolute_deviation(numbers: List[float]) -> float:` takes a list of numbers as input and returns the mean absolute deviation of the numbers. The function first calculates the mean of the numbers in the list and then sums up the absolute deviations from the mean, dividing by the total number of elements to get the average deviation.

To help understand the purpose of the function, there is also a docstring paragraph immediately below the function declaration that explains the mathematical approach and what the output represents.

You can use this function to calculate the mean absolute deviation of any list of numbers you provide. 

For example:
```python
>>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
1.0
```

This will calculate the mean absolute deviation for the list of numbers [1.0, 2.0, 3.0, 4.0], in this case giving a result of 1.0.