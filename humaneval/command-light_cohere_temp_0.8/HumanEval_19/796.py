```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are none of them.
    """ Return as as 'zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'.
    return numbers.map(lambda x: x if x <= "five" else x.map(lambda n: str(n) if n.isdigit() else 4))
```