```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return sorted(numbers.split())
numbers.str(map(int, numbers.Itout))
convert to int and sort as described above.
    """
Test cases:
>>> sort_numbers('three onefive')
'one threefive'
>>> sort_numbers('169')
'seven eight ten nine'
```