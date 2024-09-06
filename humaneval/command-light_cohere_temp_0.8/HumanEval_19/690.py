```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split(' ',numbers).
          numbers = [map(numbers)
          numbers = [int(num) for num in numbers.
          return ''.join(sorted(numbers))
          return numbers
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('abc 123 456') == '123 456 abc'
    assert sort_numbers('zero eight seven six') == 'zero eight seven six'
    assert sort_numbers('six three four') == 'six three four'
    assert sort_numbers('10 99') == '10 99'
    assert sort_numbers('nine') == 'nine'
    return 'success'
```