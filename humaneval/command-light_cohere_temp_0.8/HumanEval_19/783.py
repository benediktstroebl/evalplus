```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.

    return numbers.split(' ')
   as numbers to integers and sort them from smallest to largest.
    """
    strings, numbers are sorted from smallest to largest
    return ''.
    """

    # tests
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('zero two three') == 'zero two three'
    assert sort_numbers('one two three four') == 'two three one four'
    assert sort_numbers('three zero seven eight') == 'zero seven eight three'
    assert sort_numbers('eight seven six') != 'zero seven six eight'
```