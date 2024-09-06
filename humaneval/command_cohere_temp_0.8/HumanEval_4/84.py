Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    deviation = sum(math.abs(x - mean) for x in numbers) / len(numbers)
    return deviation
```

This function `mean_absolute_deviation(numbers: List[float]) -> float:` calculates the mean absolute deviation of a list of numbers. It first calculates the mean of the numbers, then iterates through the list, calculates the absolute deviation from the mean for each number, and sums these deviations, dividing by the total count to get the average deviation.

The result is the mean absolute deviation, which provides a measure of the spread or variability of the dataset, appreciating both positive and negative deviations from the mean. 

You can use this function to get the mean absolute deviation of any list of numbers you provide. 
It also includes a docstring to explain the purpose of the function, the formula used, and an example of use, so you can use it as documentation for future users. Likely, you can utilize it in unit tests as well.