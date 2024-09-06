```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(num) for num in numbers.
    numbers.sort()
    Settings are numbers in descending order
    Return a sorted string
    """
    return numbers_sorted_string(numbers)


def numbers_sorted_string(numbers):
    return ' '.join(str(num) for num in sorted(numbers))

# Test the sort_numbers function with sample inputs
test_sort_numbers = """
def test_sort_numbers(numbers: str) -> None:
    return sort_numbers(numbers) == 'two three four five six seven eight nine'
test_sort_numbers(' seven eight nine zero one two three ')
```
This script defines a function `sort_numbers` that sorts a list of numbers in descending order and tests it with sample inputs.  The expected output of this code is `two three four five six seven eight nine`.