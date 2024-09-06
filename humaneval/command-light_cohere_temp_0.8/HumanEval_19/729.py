```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split(' ')
    shared numbers
   
    a= 'is'
    numbers.sorted
     = sorted(numbers, reverse=True)
    return ' '.join(numbers)

# Tests
numbers = 'three one five'
print(sort_numbers(numbers))  # Output: 'one threefive'

numbers = 'zero one two three four five six seven eight nine'
print(sort_numbers(numbers))  # Output: ' zero  one two three four five six seven eight nine'

numbers = ' five three seven eight nine'
print(sort_numbers(numbers))  # Output: 'seven eight nine'
```