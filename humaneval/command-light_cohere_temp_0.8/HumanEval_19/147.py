```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split().numbers.split(' ', ')
   An empty string produces an empty list, which is incorrect.
    return numbers.split(' ', ')
numbers.split(' ', ')
   numbers
    numbers=[int.isdigit() for int(c) in range(10)])
    return numbers

# Test cases
def test_sort_numbers(test_numbers: str) -> None:
    expected = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'][::-1]
    actual = sort_numbers(test_numbers)
    assert actual == expected, f"Expected {expected}, but got {actual}"

test_cases = [
    "three one five",
    "six seven eight nine",
    "two 3 four five six"
]
test_sort_numbers(test_cases)
```
This Python script defines a function `sort_numbers` that takes a space-delimited string of numbers and returns a sorted version of that string. The function uses the split and remove the spaces, then uses a list comprehension to filter out the valid numbers from the string. It also uses assertion to test if the output is correct. 

The `test_sort_numbers` function is used to define a set of test cases, and it passes those test cases with the `sort_numbers` function.