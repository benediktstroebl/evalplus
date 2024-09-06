```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split(' ')
    Merely a converting to an integer list and sorting in ascending order.
    """
    after: 

    Here's a breakdown of the process:
    - The function takes a string as input, which is divided into spaces using `split(' ')` and stores the resulting array of spaces.
    - Each number in the list is then converted to an integer using `int()` function.
    - Finally, the `sorted()` function is used to sort the numbers in ascending order.
    - Finally, the sorted numbers are converted back to a string using `join()` method and returned as a string.

This function efficiently sorts a list of numbers in ascending order using Python's built-in `sorted` function. It is takes advantage of the `typing` to ensure type-specific operations.