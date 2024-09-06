```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split(' ', numbers). string.
    return 'numbers numbers sorted from smallest to largest
    numbers = sorted(numbers)
    return ' '.join(numbers)
    # Test case
    numbers = "three one five"
    print(sort_numbers(numbers))
    # Expected output: 'one three five'
```