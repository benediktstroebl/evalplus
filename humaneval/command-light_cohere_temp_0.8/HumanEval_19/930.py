```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    return numbers.split(' ', ')[:-1] \
           .sort() \
           .replace(' ', '') \
           .join('')
```
This Python code defines a function `sort_numbers` that takes a string of numbers separated by spaces as input and returns a string with numbers sorted from smallest to largest in ascending order. The function uses the basic string manipulation and the `split` method to split the input string into a list of numbers, then uses the `sort` method to sort the numbers in ascending order. The function also uses the string replacement to remove any spaces from the sorted numbers string.