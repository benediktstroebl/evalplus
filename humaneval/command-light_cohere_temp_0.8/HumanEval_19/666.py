```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = numbers.split()
   
    values = [int(num) for num in numbers if num.isdigit()]
    regEx = r'([0-9])'
    filtered_numbers = [num for num in numbers if regEx.match(num)]
    if not filtered_numbers:
        raise ValueError('Input string does not contain any numbers.')
    return ''.join [num for num in filtered_numbers if num in numbers]
    return ' '.join(sorted(numbers))

# Unit tests
numbers = "three one five".split()
test_sort_numbers = [sort_numbers(numbers)]
assert test_sort_numbers == ['one', 'three', 'five']
```