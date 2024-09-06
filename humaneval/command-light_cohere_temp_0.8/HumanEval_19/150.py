```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(c) for c in numbers.
    return ' '.join(sorted(numbers))
numbers = ['three one five', 'two three eight', 'six four nine']
result = sort_numbers(numbers)
print(result)
```
This code defines a function sort_numbers that takes a string of numbers separated by spaces as input and returns a new string with the numbers sorted from smallest to largest. The function uses a list comprehension to convert the input string into a list of numbers, and then sorts the list using the sorted() method. The sorted numbers are then joined together with spaces to form the final result, which is then printed to the console.