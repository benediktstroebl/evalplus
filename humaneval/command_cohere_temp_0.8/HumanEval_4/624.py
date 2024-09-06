Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    dev = sum(math.abs(x - mean) for x in numbers) / len(numbers)
    return dev
```

This function `mean_absolute_deviation(numbers: List[float]) -> float:` takes a list of numbers as input and returns the mean absolute deviation of the numbers. The function first calculates the mean of the numbers in the list and then sums up the absolute deviations from the mean, dividing by the total number of elements to get the average.

To help understand the functionality, here's a simple usage example that can be executed with this script:
```python
test_mean_absolute_deviation = [
    ([] , None),
    ((1.0, 2.0, 3.0, 4.0), 1.0),
    ((1.0, 2.0, 3.0, 5.0, 4.0), 2.0),
]

for n, ex in test_mean_absolute_deviation:
    assert mean_absolute_deviation(n) == ex
```
This would assert that the function behaves as expected for the sample cases provided.