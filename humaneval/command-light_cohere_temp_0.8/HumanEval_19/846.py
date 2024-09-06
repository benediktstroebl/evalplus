Here's the self-contained Python function:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'. Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(x) for x in numbers. Return the string with numbers sorted from smallest to largest
    """
    return numbers.sort()
```

Here are some tests for the function:
```python
>>> sort_numbers('three one five')
'one three five'
>>> sort_numbers('six three eight')
'six three eight'
>>> sort_numbers('9 six 5')
'six nine 5'
```