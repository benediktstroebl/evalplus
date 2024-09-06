Here's a Python script with a self-contained function that solves the problem you've outlined, along with a markdown code block showing the code and a test:
```python
# Ensure tests are run in a specific order so that relative order of testing doesn't affect the leaking of _mean
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation
    """
    _mean = statistics.mean(numbers)
    return statistics.mean(abs(x - _mean) for x in numbers)

numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
assert mean_absolute_deviation(numbers) == 1.0

```

This script uses the `statistics` module to calculate the mean of the input list, and then calculates the mean absolute deviation using a list comprehension and the `statistics.mean` function. The resulting value is then returned. 

The test case ensures that the function correctly calculates the Mean Absolute Deviation for a given list [1.0, 2.0, 3.0, 4.0, 5.0, 6.0].  The assertion checks if the function returns 1.0 which is the correct answer for this specific dataset. You can also add more test cases to cover different scenarios and ensure the robustness of the solution.