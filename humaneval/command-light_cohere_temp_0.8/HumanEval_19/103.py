```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers. It uses Python list comprehension to sort the numbers from smallest to largest, and join them with spaces."""

# Example function call and test cases
numbers = "three one five"
sorted_numbers = sort_numbers(numbers)
print("Sorted numbers:", sorted_numbers)

numbers = "two three seven eight"
sorted_numbers = sort_numbers(numbers)
print("Sorted numbers:", sorted_numbers)

numbers = "two 9 eight six three"
sorted_numbers = sort_numbers(numbers)
print("Sorted numbers:", sorted_numbers)
```