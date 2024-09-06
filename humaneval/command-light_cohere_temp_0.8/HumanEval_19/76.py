```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'. Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split(' ')
    however, numbers may contain duplicates
    """
    numbers = numbers.split(' ')
    delimiters = numbers.filter(lambda x: x != ' ')
    numbers = [int(x) for x in numbers if x.isdigit()]
    .sort()
    return ' '.join(numbers)
```