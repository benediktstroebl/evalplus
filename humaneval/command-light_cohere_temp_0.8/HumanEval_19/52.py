```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(n) for n in numbers.
    return ' '.join([str[i] for i in sorted(numbers)])
    return numbers
numbers_list = ['three one five', 'two three eight', 'seven six three']
print(sort_numbers(numbers_list))  # Expected output: one three five, two three eight, seven six three
```