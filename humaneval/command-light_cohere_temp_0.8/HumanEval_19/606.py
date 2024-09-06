```python
import pytest
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    return sorted(set(map(int, numbers. )))


# Example of function usage and testing
numbers = 'three one five six seven eight nine'
result = sort_numbers(numbers)

# Test if the function works as expected
assert len(result) == 10, "Failed to sort the list of numbers"

pytest.names = ["sorted_numbers_test"]

# Run the tests
pytest.names = List(pytest.marknames)
run(sort_numbers, __name__)
``` 
This script defines a function **sort_numbers** that sorts a list of numbers in alphabetical order. It uses a set and map functions to convert the string of numbers into a list of integers, which are then sorted using the **sorted** function. The test suite consists of one function **sorted_numbers_test** that passes the function the numbers string and asserts that the resulting list has a length of 10.