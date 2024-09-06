```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Numbers are sorted from smallest to largest.
    Return the value of the
    a list of strings, with each string representing a number.
    """
    first_number = 0
    numbers_str = "".join(numbers.split())
    numbers_list = []
    for num in numbers_str:
        numbers_list.append(int(num))
    numbers.sort()
    value=None
    is_valid = True
        for num in numbers:
            if is_valid and num == first_number:
                is_valid = False
                first_number = num
        if is_valid:
            numbers_list.append(first_number)
        first_number += 1
    numbers_str = ', '.join(map(str,numbers_list)))
    return numbers_str
```