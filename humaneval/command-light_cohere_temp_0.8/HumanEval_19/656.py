```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    >>> sort_numbers('ZeroTwoThreeFourFiveSix')
    'ZeroTwoThreeFourFiveSix'
    >>> sort_numbers('1010111')
    Traceback (most recent call last):
    ...
    ValueError: Only supported strings with numbers may be passed to sort_numbers().
    """
    if not isinstance(numbers, str):
        raise ValueError("Only supported strings with numbers may be passed to sort_numbers.")

    numbers = numbers.split()
    if not numbers or split():
        return numbers[0]

    numbers = [int(num) for num in numbers]
    return ' '.join(sorted(numbers)) + ' '

```