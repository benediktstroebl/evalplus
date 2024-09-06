```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return sorted(numbers.split(' '))
 sort using the digits in numbers, from smallest to largest
    """
    return sorted(numbers.split(' ')[1:])
```
The function takes a string of numbers, then splits the string to remove the separators. Then, it sorts the numbers using their digits and returns the sorted numbers.