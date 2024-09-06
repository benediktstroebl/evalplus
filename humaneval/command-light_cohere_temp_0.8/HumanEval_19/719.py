```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split()
   p numbers_
    list to string format and then return the numbers sorted from smallest to largest 
    """
    return numbers.split() 

 numbers = ['three one five']
    return sort_numbers(" ".join(numbers))  # This will return "one three five" as expected
```