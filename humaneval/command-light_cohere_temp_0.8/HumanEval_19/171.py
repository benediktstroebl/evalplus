```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split().numbers.split().numbers
    brother,numbers.all in list of afirst in the list of numbers.numbers is anumbers from smallest number to the last in the string.numbers are then in theorder of the numbers, and it is a valid input."""

numbers = "three one five"

# convert string to list
numbers = numbers.split()

# sort the list of numbers
numbers.sort()
# join the list of numbers into a string
numbers = ' '.join(numbers)

# pass the test
print(numbers)
```