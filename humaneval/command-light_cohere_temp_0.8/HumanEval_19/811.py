```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are numbers are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'.
    return numbers. If numbers contains non- valid numbers, raise ValueError. Otherwise, return the numbers sorted from smallest to largest.

test_sort_numbers = []
test_numbers = ['three one five', 'zero seven eight', 'one two three', 'four six eight']

for num in test_numbers:
    if set(num) != set(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        test_sort_numbers.raise ValueError('Invalid input')
    test_numbers.raise ValueError('Invalid input')

print('Tests passed')

return sort_numbers('five six three')
```