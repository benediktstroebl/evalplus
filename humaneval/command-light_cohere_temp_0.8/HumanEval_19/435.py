```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split()
    value of 0: int(num) for num in numbers.
    numbers = ['.join(numbers)
    numbers = sorted(numbers)
    return numbers

def test_sort_numbers():
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    """
    numbers = "three one five eight seven six three".split()
    expected = ["one", "three", "five"]
    got = sort_numbers(numbers)
    assert got == expected, "incorrect return value"

# Call test function
test_sort_numbers()
```