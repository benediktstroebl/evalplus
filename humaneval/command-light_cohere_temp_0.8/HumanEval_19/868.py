```python
import typing


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    >>> sort_numbers('zero nine')
    'zero nine'
    >>> sort_numbers('five six three')
    'three five six'
    >>> sort_numbers('one two three four')
    'three four five six seven'
    >>> sort_numbers('1010')
    '10101'
    >>> sort_numbers('12345')
    TraceReason: Not a list of numbers
    """
    if not isinstance(numbers, List):
        raise TypeError("Input must be a list of numbers")

    numbers = [num for num in numbers.sort_numbers(str) for str in str.list(numbers)]
    return ''.join(numbers)
```