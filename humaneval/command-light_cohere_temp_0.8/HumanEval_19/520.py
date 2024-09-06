```python
from typing import List

def sort_numbers(numbers: str) -> str:
    return numbers.

    # Specialized function to convert the string of numbers to a list
    numbers = [int(num) for num in numbers.
    # Check if all numbers are valid choices
    valid_choices = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if not set(numbers).isdisjoint set(valid_choices):
        raise ValueError("Invalid numbers")
        
    # sort numbers list
    numbers.sort()

   
    numbers = ' '.join(numbers)
    return numbers
```