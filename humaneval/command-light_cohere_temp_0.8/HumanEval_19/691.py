```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = numbers.split()
    arrange_numbers(numbers)
    return numbers[::-1].join()

def arrange_numbers(numbers):
    if not numbers:
        raise ValueError("Input cannot be empty")
    return numbers

numbers = ['three', 'one', 'five']
sorted_str = sort_numbers(numbers)
print(sorted_str)
arrange_numbers_again(numbers)
```