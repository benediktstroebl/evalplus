```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split()
    ** time.map_to_string(numbers), then sort and join the list
    """
    numbers = numbers.split()
   
    raw_numbers = []
    for num in numbers:
        if num not in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
            raise ValueError("Invalid input. The number {} is not in the list of valid numbers.".format(num))
        raw_numbers.append(int(num))
    return ' '.join(map(str, raw_numbers))
```
This script defines a function `sort_numbers` that sorts a list of numbers from smallest to largest. The function takes a input in the form of a string of numbers separated by spaces. It then splits this string into individual numbers and sorts them into a list. Then, it maps each number to its string representation and finally joins them back into a string.