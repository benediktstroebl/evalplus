```python
import pytest
from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split()
    fact list of a string to be split into a list of numbers, then sort the list and join the sorted numbers back into a string."""


def test_sort_numbers() -> None:
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("zero one two three four five six seven eight nine") == "zero eight seven six five four three two one"
    assert sort_numbers("10999") == " nine  nine eight seven six"
    assert sort_numbers("abc123") == "123abc"
    assert sort_numbers("") == ""
    assert sort_numbers("9") == "nine"
    assert sort_numbers("-1") == "-one"
    return


if __name__ == "__main__":
    pytest.test_sort_numbers()
``` 
This script includes a `sort_numbers` function that takes a string of numbers and returns a sorted version of that string. It also includes a test function to run the `sort_numbers` function and assert its results against expected values. The `pytest` library is used to provide a simple and concise way to write test cases.