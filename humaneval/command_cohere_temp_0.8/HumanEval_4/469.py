Here's a Python script with a self-contained function that solves the problem you've outlined, along with a separate test module to validate its correctness:
```python
# module code
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    if not numbers:
        raise ValueError("Input list is empty")
    
    mean = sum(numbers) / len(numbers)
    deviations = [abs(num - mean) for num in numbers]
    return sum(deviations) / len(deviations)

# unittest style tests
def test_mad_with_single_number():
    """ Tests mean_absolute_deviation() with a single number list """
    assert mean_absolute_deviation([1.0]) == 0.0

def test_mad_with_two_numbers():
    """ Tests mean_absolute_deviation() with a list of two numbers """
    assert mean_absolute_deviation([1.0, 2.0]) == 1.0

def test_mad_with_three_numbers():
    """ Tests mean_absolute_deviation() with a list of three numbers """
    assert mean_absolute_deviation([1.0, 2.0, 3.0]) == 1.0

def test_mad_with_all_same():
    """ Tests mean_absolute_deviation() with a list of identical numbers """
    assert mean_absolute_deviation([1.0, 1.0, 1.0]) == 0.0

def test_mad_with_negative_numbers():
    """ Tests mean_absolute_deviation() with a list containing negative numbers """
    assert mean_absolute_deviation([1.0, -2.0, 3.0, -4.0]) == 4.0

def test_mad_with_large_numbers():
    """ Tests mean_absolute_deviation() with a list containing large numbers """
    assert mean_absolute_deviation([10000.0, 10001.0, 10002.0]) == 1.0

def test_mad_with_empty_list():
    """ Tests mean_absolute_deviation() with an empty list """
    with pytest.raises(ValueError):
        mean_absolute_deviation([])

```

The `mean_absolute_deviation` function calculates the Mean Absolute Deviation as per the problem statement.

The test module uses the `pytest` framework, which simplifies test writing and execution. It validates the behavior of the `mean_absolute_deviation` function against various test cases, such as lists with single or multiple numbers, negative numbers, large numbers, and an empty list.

To run the tests, ensure you have `pytest` installed (`pip install pytest`), and execute the command `pytest test_mad.py` in your terminal. 

This script should help you efficiently solve the problem and validate its correctness using automated tests. Let me know if you have any further questions or need additional assistance!