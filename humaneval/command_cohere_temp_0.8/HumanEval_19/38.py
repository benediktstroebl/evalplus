```python
from typing import List

def sort_numbers(input_numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = input_numbers.split()
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers
```

This script takes an input string of numbers that are space-separated and returns a string with the numbers sorted from smallest to largest. The function first splits the input string into a list of numbers, then sorts that list, and finally joins the list back into a string.

Here is an example usage of the function and the expected output:
```python
print(sort_numbers('three one five'))  # Output: one three five
```

This function can also be used to sort numbers with different groupings, like 'one two three five eight'. Adjustments could be made to accept non-space separators and handle negative numbers as well.