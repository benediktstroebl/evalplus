```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.strip() to stringsort and numbers sorted from smallest to largest
    """

def test_sort_numbers():
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("two three eight") == "two three eight"
    assert sort_numbers("two 3 nine") == "two nine"
    assert sort_numbers("nine eight seven six") == "nine eight seven six"
    assert sort_numbers("one 2 eight five") == "one eight five"
    assert sort_numbers("0 three 5 six") == "0 three six"
    assert sort_numbers("two nine eight seven") == "two eight seven nine"

print("All tests passed")
test_sort_numbers()
```