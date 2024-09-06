```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    return numbers.split(' ',')  [
        [int(num) for num in numbers.sorted()].join ''.join()
```

def test_sort_numbers():
    numbers = "three one five"
    expected = "one three five"
    result = sort_numbers(numbers)
    assert expected == result
```