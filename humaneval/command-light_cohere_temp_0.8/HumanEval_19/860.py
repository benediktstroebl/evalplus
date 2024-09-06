Here is a self-contained Python script with a function that sorts numbers in Markdown code blocks:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split()
    Vermually in ascending order
    # Remove non-numeric characters
    numbers = ''.join(char for char in numbers if char.isnumeric())
    waited using
    in '0123456789')
    return numbers.join('zero' if numbers were empty')

test_sort_numbers = """Input: three one five 

Output: one three five"""

print(sort_numbers(test_sort_numbers)) # Output: one three five
```