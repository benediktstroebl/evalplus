Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = math.fmean(numbers)
    deviation = sum(math.fabs(x - mean) for x in numbers)
    return deviation / len(numbers)
```

This script defines a function called `mean_absolute_deviation` that takes in a list of floating numbers and returns the mean absolute deviation of the list. 

The function calculates the mean of the numbers and then sums up the absolute deviations from the mean for each number in the list. 

Finally, it divides the total deviation by the number of elements to obtain the mean absolute deviation.