```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    format: B
>>> sort_numbers('three one five')
'one threefive'
    """
    numbers = [int(num) for num in numbers.
    return "".join(sorted(numbers))
# Unit tests
def test_sort_numbers():
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("zero twelve three") == "012"
    assert sort_numbers("Guru 90 four") == "four eight nine"
    assert sort_numbers(" ") == ""
test_sort_numbers()  # Run tests
```
The provided code defines a Python script with a self-contained function `sort_numbers` that sorts a list of numbers in ascending order. The function takes a string of numbers as its argument, converts it into a list of integers, and then sorts the list using the sorted() function. 

The test_sort_numbers function contains unit tests that check the correctness of the `sort_numbers` function by passing various test cases. 

The `typing` module is used to provide type hints for functions and variables, which can improve the readability and maintainability of the code.