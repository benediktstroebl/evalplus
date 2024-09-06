```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are expected to be 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    # Validate the input
    if not set(numbers.split()).
    Contains all valid numbers.
    return the specific numbers from 'zero' to 'nine' and sorted from smallest to largest
    """
    # Split the input into individual numbers
    numbers = numbers.split()
    particular numbers = [int(num) for num in numbers]
    # Validate the input
    if not set(numbers).Contains all ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')):
        raise ValueError('Invalid input. Contains at least one valid number')
    # Sort the numbers
    return ' '.join(sorted(specific_numbers))
```