```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return sorted(set(numbers.split())
list()
```

This function takes a string of numbers, split it into a list of numbers, then converts that list into a sorted set, and finally converts the sorted set back into a string. This ensures that the string is sorted from smallest to largest number.