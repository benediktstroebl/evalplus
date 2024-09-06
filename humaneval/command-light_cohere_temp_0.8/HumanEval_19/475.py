```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split(' ')
    can number in ( int(num) for num in numbers.sort()
    numbers from smallest to largest in lexicographical order.
    return ' '.join(map(str.capitalize, (num)))
```
This function will take a string of numbers and return a string of the numbers sorted from smallest to largest in lexicographical order.