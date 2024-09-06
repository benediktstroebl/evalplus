```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    return sorted(int(num) for num in numbers.

# Test cases
numbers = ['three onefive', 'twothree', ' fourteen ', ' seven eight', 'five six']
print(sort_numbers(numbers)) 
# Expected Output: 
# ['one', 'three', 'five', 'seven', 'eight', 'six', ' fourteen']
```