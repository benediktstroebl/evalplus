```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(num) for num in numbers. Sort the numbers from smallest to largest
    return the string with numbers sorted
    """
    return numbers().ol(sorted(numbers))

numbers = "three one five"

print(sort_numbers(numbers))
``` 
This code will sort the numbers three, one, and five and print the result, which will be "one three five".