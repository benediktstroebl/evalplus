```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(num) for num in numbers.
    numbers.sort()
    offering: list of numbers sorted from smallest to largest
    numbers_str = ', '.join(str(num) for num in numbers))
    return numbers_str

numbers = 'three one five '
print(sort_numbers(numbers))  # expected output: one three five'
```
This Python script defines a function called sort_numbers that takes a space-delimited string of numbers as input and returns a new string with the numbers sorted from smallest to largest. The function first converts each input string into a list of integers and then sorts this list using the sort() method. The sorted list is then joined with a comma to create the final output string.