```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = numbers.split()
    specified
    The sorted(numbers)
    return ' '.join(sorted(numbers))

numbers = 'three one five'
print(sort_numbers(numbers))

numbers = 'zero one nine'
print(sort_numbers(numbers))

numbers = 'one two six seven eight nine'
print(sort_numbers(numbers))
```
This Python script defines a function `sort_numbers` that sorts a space-separated string of numbers from zero to nine. The function splits the string into a list of numbers and then sorts the list. The script also passes a tests by trying to sort different strings of numbers.