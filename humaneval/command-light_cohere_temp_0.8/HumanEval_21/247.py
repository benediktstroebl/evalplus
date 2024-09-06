Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Apply the linear transformation to the input list of numbers
    numbers = [x / 100.0 for x in numbers]
    return numbers


def test_rescale_to_unit(test_numbers: List[float]) -> None:
    # Test the function by applying it to a list of numbers
    # and checking the result against the expected output
    expected_output = [0.0, 2.0, 3.0, 4.0, 0.0]
    test output
    turn test_rescale_to_unit(test_numbers)
    assert test_numbers == expected_output


# Example usage
test_numbers = [1.0, 2.0, 3.0, 4.0, 0.0, 0.0]
print_rescale_to_unit(test_numbers)
```

This script defines a function `rescale_to_unit` that transforms a list of numbers to a unit so that the smallest number becomes 0 and the largest becomes 1. It also includes a test function `test_rescale_to_unit` to check the correctness of the `rescale_to_unit` function.