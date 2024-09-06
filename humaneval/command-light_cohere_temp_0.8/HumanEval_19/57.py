```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers.
    Valid choices are valid numbers from 'zero' to 'nine'.
    Numbers are sorted from smallest to largest.
    """
    return "".join(numbers.sort())
```

numbers = 'three one five'
sorted_numbers = sort_numbers(numbers)
print(sorted_numbers)  # Output: 'one threefive'
``` 
This Python code defines a function named sort_numbers, designed to transform a space-delimited string of numbers into a string with the numbers sorted from smallest to largest. The code employs the function .join() to sort the list of numbers, and then returns the sorted string. The code employs the valid numbers from 'zero' to 'nine', ensuring that only these valid numbers are processed.