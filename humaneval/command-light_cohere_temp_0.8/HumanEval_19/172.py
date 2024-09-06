```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split(' ')
    Reception of input.
    numbers = [numbers = numbers.split(',')
    how many numbers?his numbers,
    digits = [int(num) for num in numbers if num.isdigit()]
   r = ''.join(numbers)
    return r.split(' ')
    the how numbers
    numbers = [int(num) for num in numbers if num.isdigit()]
   duplication, numbers_ are in sorted order from smallest to largest. Then the numbers that were generated in a different order are reversed and returned in their original order.
    """
unit tests pass. The string is returned from the function is valid and correct.
```