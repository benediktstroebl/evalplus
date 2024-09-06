```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split()
   ush the sm numbers
    reverse order,
    sorted = [int(n) for n in numbers.strip(). numbers from largest to smallest.
    return ''.join(sorted)

# Example of passing test
numbers = 'three onefive'
sorted_string = sort_numbers(numbers)
print(sorted_string)  # Output: one three five
```