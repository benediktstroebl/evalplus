```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are string is 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(x) for x in numbers.
    return f" numbers { '0 3 5 6 7 8 9' if numbers <= ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] else 'Invalid input')

# Test cases
numbers1 = 'three one five'
numbers2 = 'zero seven eight'

print(sort_numbers(numbers1))  # Output: 'one threefive'
print(sort_numbers(numbers2))  # Output: 'zero78'

numbers3 = 'abc123'
numbers4 = 'one two three'

print(sort_numbers(numbers3))  # Output: 'one two three abc123'
print(sort_numbers(numbers4))  # Output: 'one two'
```