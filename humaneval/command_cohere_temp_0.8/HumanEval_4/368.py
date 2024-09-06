Here's a Python script with a self-contained function that solves the problem you've outlined, along with a separate test module to validate its correctness:
```python
# module: utilities.py
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation value
    """
    mean = math.mean(numbers)  # Mean of the dataset
    deviation = sum(math.abs(x - mean) for x in numbers)  # Sum of absolute deviations
    return deviation / len(numbers) if len(numbers) > 0 else 0

# Tests
def test_mad():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0
    assert mean_absolute_deviation([2.0, 2.0, 2.0, 2.0, 5.0]) == 1.0
    assert mean_absolute_deviation([0.0, 0.0, 0.0, 0.0, 0.0]) == 0.0
    assert mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]) == 4.0
    assert mean_absolute_deviation([10, 20, 30, 40, 50]) == 15.0

test_mad()
```
You can copy and paste this code into two separate Python files: `utilities.py` and `test_utilities.py`. After doing so, you can run the test file to verify that the `mean_absolute_deviation` function produces the expected outputs for various inputs.