```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are string contains only digits 0-9.
    The expected output is a sorted version of numbers
    """
    numbers = [int(x) for x in numbers.
    return ''.join(numbers).
    return f'{" {sorted(numbers)}"
    ```