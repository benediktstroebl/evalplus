```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are valid are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = [int(x) for x in numbers.
    return ' '.join(sorted(numbers))

# Tests
def test_sort_numbers():
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('Zero Two Three Four Five Six Seven Eight Nine') == 'Zero Two Three Seven Eight Nine'
    assert sort_numbers('AOneTwoThreeFourFiveSix') == 'OneTwoThreeFourFiveSix'
    assert sort_numbers('one two three four five six seven eight nine') == 'one two three four five six seven eight nine'
    return
test_sort_numbers()
 ```