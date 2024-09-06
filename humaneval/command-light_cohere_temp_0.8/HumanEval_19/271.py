```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return sorted_numbers_desc(numbers)

def sorted_numbers_desc(numbers: str) -> str:
    return numbers.

numbers = "three one five"
print(sort_numbers(numbers))  # Output: 'one threefive'
``` 
This script defines a function `sort_numbers` that takes a string of numbers in `numbers` as input, and returns the string of numbers sorted from smallest to largest. 
The `sorted_numbers_desc` function is a helper function that applies the sorting operation. 
It uses Python's built-in `sorted` function with the `reverse` parameter to sort the numbers in descending order.