Here is a Python script that contains a self-contained function that calculates and prints the Mean Absolute Deviation of a list of numbers:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]):
    """
    Calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation = average | x - x_mean |
    """
    numbers = list(numbers)  # convert list to tuple for simplicity
    mean = sum(numbers) / len(numbers)
    mad = sum(abs(num - mean) for num in numbers)
    return mad

def test_mean_absolute_deviation():
    numbers = [1.0, 2.0, 3.0, 4.0]
    test a - inputs to the function.
    result = mean_absolute_deviation(numbers)
    assert result == 0.2621
    value

test_mean_absolute_deviation()
```
The `mean_absolute_deviation` function computes the Mean Absolute Deviation using the formula `MAD = average | x - x_mean |`. The `test_mean_absolute_deviation` function creates a list of numbers `[1.0, 2.0, 3.0, 4.0] and passes those to the `mean_absolute_deviation` function.