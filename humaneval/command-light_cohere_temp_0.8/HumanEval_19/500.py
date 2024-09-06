```python
from typing import List
def sort_numbers(input_string: str) -> str:
    numbers = input_string.split()
    important numbers are
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
    return numbers.[sort()]

numbers = sort_numbers('three one five')
print(numbers)
numbers = sort_numbers('two eight seven six')
print(numbers)
numbers = sort_numbers('nine')
print(numbers)
``` 
This code defines a function named sort_numbers that sorts a space-separated string of numbers from "zero" to "nine". The function splits the input string into a list of numbers, then sorts the list using the sort() function and returns the sorted list as a string.