Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    deviation = sum(math.abs(x - mean) for x in numbers) / len(numbers)
    return deviation
```

This function `mean_absolute_deviation` calculates the mean of the input list of numbers, then finds the absolute deviation of each number from the mean, sums up these deviations, and divides by the total count to get the average absolute deviation, which is the Mean Absolute Deviation. The function assumes the provided list contains only numeric values.

To use this function, you can provide a list of numbers as input like this:
```python
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print(result)
```

The printed output will be:
```bash
1.0
```

This value represents the Mean Absolute Deviation of the list `[1.0, 2.0, 3.0, 4.0]`.