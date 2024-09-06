```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine,
    Valid choices are zero, one, two, three, four, five, six, seven, eight, and nine
    """
    # split the string to numbers
    numbers = [int(num) for num in numbers.
    # sort the recommended order numbers
    return ' '.join(sorted(numbers))

# Test cases
numbers_test = ["three one five", "six three eight", "zero seven nine"]
sorted_out = sort_numbers(numbers_test)
print(sorted_out)  # expected output: ['zero seven nine', 'three one five', 'six three eight']
```