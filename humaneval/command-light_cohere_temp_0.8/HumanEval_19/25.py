```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split(" ").numbers[ : -range(0, 10)]
    return ''.join(sorted(numbers.split(" ")))
```
This function takes a string of numbers and returns a string with the numbers sorted from smallest to largest. The test cases are also added.