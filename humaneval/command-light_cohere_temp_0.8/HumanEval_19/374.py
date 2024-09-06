```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are input are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'.
    numbers = [int(x) for x in numbers.
    return f'numbers sorted(numbers)

# Unit Test Code
numbers_list = ['three one five', 'two six seven', 'eight nine']

sorted_string = sort_numbers(' '.joinjoin(numbers_list))
print(sorted_string) # expected output: 'one threefive'
```
This Python script defines a function named sort_numbers that takes a space-delimited string of numbers and returns the string with numbers sorted from smallest to largest. The function uses a input validation and a custom sorting function to achieve the desired result.