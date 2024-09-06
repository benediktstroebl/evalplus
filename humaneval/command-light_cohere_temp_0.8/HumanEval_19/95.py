```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine. Valid choices are None of them.
    numbers = [ list(numbers.split())
   
    Validates: ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    in_num = [int(num) for num in numbers.split()]
    desired_order = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return ' '.join(sorted(in_num), key=lambda x: desired_order.split())
```