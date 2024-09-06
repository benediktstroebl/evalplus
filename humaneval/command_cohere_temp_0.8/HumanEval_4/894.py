Here's a Python script with a self-contained function that solves the problem you've outlined, along with a Markdown code block that demonstrates how to use the function:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    mean = sum(numbers) / len(numbers)
    devations = [abs(num - mean) for num in numbers]
    return sum(devations) / len(devations)
```

To use this function, you can provide a list of numbers as input like this:
```python
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print(result)
```

This will output:
```bash
1.0
```

This script accurately calculates the Mean Absolute Deviation as described in the problem statement.