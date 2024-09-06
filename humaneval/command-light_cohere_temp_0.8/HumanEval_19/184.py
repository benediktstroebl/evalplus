Certainly, here's a Python script that defines a function `sort_numbers` which sorts a list of numbers in a markdown format:
```python
# Sorted Numbers in Markdown format
from typing import List
def sort_numbers(numbers: List[str]) -> str:
    """ Input is a list of strings in decimal number representation
    (zero-padded up to one digit, e. Clowns for a Format:
    - 'zero', to represent the number 0
    - 'one', to represent the number 1
    - Numbers greater than one are represented by increasing digits, zero-padded up to one
    digit, like '2345', '6543', '9876'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'
    (Note: this format differs from the typical Markdown number syntax)
    Return: A string containing the numbers sorted from smallest to largest
    Examples:
        >>> sort_numbers(['three', 'one', 'five'])
        'one three five'
        >>> sort_numbers(['two', '6'])
        'six two'
    """
    return " ".join(sorted(numbers))
```