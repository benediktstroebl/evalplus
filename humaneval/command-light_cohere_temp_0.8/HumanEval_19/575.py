```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split().list(numbers).getitem.
    if itgetnumbers anynumber if digits in the string.
    return ''.join(sorted(items))
numbers = 'three one five'
print(sort_numbers(numbers))  # Output: 'one threefive'
``` 
This script defines a function `sort_numbers` that takes a string of numbers as input and returns the sorted version of those numbers. The function uses the split to separate the numbers into a list, then sorts the list using the `sorted` function and joins the sorted items back into a string.