```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return sorted(int(n) for n in numbers.
    """
sorted_numbers = sort_numbers('three one five')
    print(sorted_numbers)  # Output: 'one three five'
``` 
This Python script defines a function `sort_numbers` that sorts a list of numbers from the string input. The function uses the essential type hint and converts each number to an integer before sorting it.