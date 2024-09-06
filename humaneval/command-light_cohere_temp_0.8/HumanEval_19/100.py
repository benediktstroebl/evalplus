Here is a self-contained Python script that defines a function sort_numbers that sorts a string of numbers in a markdown code block:
```python live_script
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split().numbers = numbers_list = numbers.split()
   UTC = 'en-US'
numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers.sort = sorted(numbers)
number_string = ', '.join(numbers)
return number_string
```