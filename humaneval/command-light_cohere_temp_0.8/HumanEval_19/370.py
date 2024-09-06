```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are
    numbers are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.

    # Sort numbers from smallest to largest
    numbers = [int(n) for n in numbers.

    # Convert numbers to list
   
    numbers = List(numbers)
    # Sort the list
    numbers.sort()
    Reverses the read order
    numbers = list(sorted(numbers))
    numbers = ' '.join(str(n) for n in numbers)

    return numbers

# Test the function
numbers = "three one five"
print(sort_numbers(numbers))  # Output: one three five"
```