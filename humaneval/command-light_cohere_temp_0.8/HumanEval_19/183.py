```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return sorted(numbers.split())
numbers.numbers = [
       numbers = numbers.split()
   numbers = [n for n in numbers]
    if len(numbers) == 0:
        return "No valid numbers found."
    elif len(numbers) == 1:
        return numbers[0]
    elif numbers[0] == "":
        return "Input must contain numbers"
    elif numbers[0].isalpha():
        return "Input must contain only numbers"
    else:
        return "Input must be something like 0-9"
```