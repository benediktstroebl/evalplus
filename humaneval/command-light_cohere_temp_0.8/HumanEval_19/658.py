```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # split the numbers
    numbers = numbers.split()
    .map(int) .sort()
    return ' '.join(numbers)

# test cases
numbers = 'three one five'
print(sort_numbers(numbers)) # 'one three five'

numbers = 'zero eight nine'
print(sort_numbers(numbers)) # 'nine eight zero'

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
print(sort_numbers(numbers)) # 'four three two one five six seven eight nine'

numbers = ['zero', 2, 4, 6, 8, 9]
print(sort_numbers(numbers)) # 'four three six eight nine zero'
```