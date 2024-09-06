Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    dev = sum(math.abs(x - mean) for x in numbers) / len(numbers)
    return dev
```

This function `mean_absolute_deviation` calculates the mean of the input list of numbers and then finds the average absolute deviation of each number from the mean. It uses Python's `typing` module to ensure type safety and the `math` module to handle absolute value calculations. The result is the mean absolute deviation of the provided list of numbers.