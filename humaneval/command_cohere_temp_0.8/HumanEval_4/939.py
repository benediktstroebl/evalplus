Here's a Python script with a self-contained function that solves the problem you've described, along with a series of tests to validate its correctness:
```python
# Importing the necessary typing module
from typing import List

# The function to calculate the mean absolute deviation of a list of numbers
def mean_absolute_deviation(numbers: List[float]) -> float:
    return sum(abs(num - sum(numbers) / len(numbers)) for num in numbers) / len(numbers)

# Here are some tests to validate the correctness of the function
def test_mean_absolute_deviation_with_list():
    # Test case 1: Basic input list with positive and negative numbers
    numbers = [1.0, 2.0, 3.0, 4.0]
    expected = 1.0
    result = mean_absolute_deviation(numbers)
    assert result == expected

def test_mean_absolute_deviation_with_list_all_negative():
    # Test case 2: List with only negative numbers
    numbers = [ -1.0, -2.0, -3.0, -4.0]
    expected = 3.0
    result = mean_absolute_deviation(numbers)
    assert result == expected

def test_mean_absolute_deviation_with_empty_list():
    # Test case 3: Empty list
    numbers = []
    try:
        _ = mean_absolute_deviation(numbers)
    except IndexError as e:
        assert str(e) == 'Cannot calculate mean absolute deviation of an empty list.'

# Run the tests when this script is directly executed
if __name__ == "__main__":
    test_mean_absolute_deviation_with_list()
    test_mean_absolute_deviation_with_list_all_negative()
    test_mean_absolute_deviation_with_empty_list()
```

In this script, the `mean_absolute_deviation` function calculates the deviation for each number in the `numbers` list, sums up the absolute deviations, and then divides by the total number of elements to get the mean absolute deviation.

The unit tests are provided to validate the correctness of the `mean_absolute_deviation` function against different scenarios. When executed, these tests will automatically verify the function's behavior against the expected output.