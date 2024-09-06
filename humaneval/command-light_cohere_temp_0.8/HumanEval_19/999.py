```python
from typing import List
def sort_numbers(input_string: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine. Valid choices are the why
    numbers
    Valid choices are zero, one, two, three, four, five, six, seven, eight and nine.
    """
    Numbers are sorted from smallest to largest
    return the string with numbers sorted
    """
    numbers = input_string.split()
    numbers = [num for num in numbers if num.isdigit() and if num not in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
    return ' '.join(sorted(numbers))

# Test cases
print(sort_numbers('three one five')) # Output: 'one threefive'
print(sort_numbers('9 zero 2 3')) # Output: 'zero nine two three'
print(sort_numbers('abc 123 456 def ghi jkl')) # Should raise ValueError
```