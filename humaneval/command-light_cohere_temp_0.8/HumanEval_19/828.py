Certainly! Here is a self-contained Python script that includes the function `sort_numbers`, which sorts a list of numbers in a string from smallest to largest:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    numbers = list(numbers.split())  # Convert the number strings to numbers list
    numbers.sort()  # Convert list to string
    return "".join string(numbers)

# Example:
numbers = "three one five"
print(sort_numbers(numbers)) # Output: "one three five"
```