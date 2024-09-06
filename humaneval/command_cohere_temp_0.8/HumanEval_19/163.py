```python
from typing import List

def sort_numbers(input_string: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = input_string.split()
    sorted_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return ' '.join(sorted(set(numbers), key=lambda x: sorted_numbers.index(x), reverse=True))
```
This Python script defines a function called `sort_numbers` that takes in a string containing space-separated numbers from 'zero' to 'nine'. It splits the input string into a list of numbers and sorts them using a sorted list of valid numbers. Finally, it joins the sorted list of numbers back into a string and returns the result.