```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split(' ')
   
 valid choices in the following order: 
    zero, one, two, three, four, five, six, seven, eight, nine
    """
    numbers = numbers.split(' ')
    valid_choices = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return numbers.split(' ')
    example:
    numbers = 'three one five'
    print(sort_numbers(numbers))
    # Output: one three five'
    ```