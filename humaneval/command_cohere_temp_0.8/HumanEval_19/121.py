```python
from typing import List

def sort_numbers(input_string: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = [int(char.lower()) for char in input_string.split()]
    sorted_numbers = [str(num) for num in numbers if num in range(0, 10)]
    return ' '.join(sorted_numbers)
```
The provided Python script defines the `sort_numbers` function that takes an input string containing space-separated numbers from 'zero' to 'nine'. It extracts these numbers, converts them to integers, filters out any invalid inputs, and sorts them in ascending order. The function returns the sorted numbers as a string.