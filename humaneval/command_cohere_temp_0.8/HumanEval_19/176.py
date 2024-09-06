```python
from typing import List

def sort_numbers(input_string: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = [int(num) for num in input_string.split()]
    sorted_numbers = [str(num) for num in sorted(numbers)]
    return ' '.join(sorted_numbers)
```

This Python script defines a function called `sort_numbers` that takes a string as input. This string contains a space-separated list of numbers from 0 to 9. The function sorts these numbers in ascending order and returns the sorted list as a string.

The function first splits the input string into a list of numbers using the `split()` method. It then sorts this list using the `sorted()` function, converting the sorted integers back to strings. Finally, the `join()` method concatenates the sorted numbers into a single string, which is returned as the result.

This implementation ensures that the function can handle different combinations of numbers correctly, sorting them from smallest to largest as expected.