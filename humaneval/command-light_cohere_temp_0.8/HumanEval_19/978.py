```python
import typing


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are return the string with numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    return numbers.split()[:-1].
            .sort()
            .join('0123456789')
            .join("")
```
This Python script defines a function `sort_numbers` that sorts a given string of numbers from smallest to largest. The function first splits the numbers by spaces, sorts the resulting list of numbers, and then joins the sorted list back into a single string. The type of input and output is specified using the `typing` module. This allows users to pass a function inputs and receive the correct output.