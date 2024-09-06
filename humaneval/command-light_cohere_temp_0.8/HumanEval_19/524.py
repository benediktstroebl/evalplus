```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are strings must only contain numbers.
    If string must be sorted from smallest to largest.
    Return the string with numbers sorted.
    """
    string is formatted to ensure comparison and readability.
    """
    using:
    - string of numbers from zero to nine.
    -   list of possible valid numbers (or strings that can be parsed as numbers)
    -   list of numbers (can have other data types)
    -   custom numbers, strings that can be parsed as numbers
    """
    # Convert string to list of numbers
    numbers = [int(num) for num in numbers.
    # Convert list of numbers to sorted list
    numbers.sort()
    string = ''.join(numbers)
    return numbers
```