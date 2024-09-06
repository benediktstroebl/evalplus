```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))
    ``` 
This script defines a function named sort_numbers that sorts a list of numbers in a string in ascending order. The function uses the number strings as input and returns the sorted list of numbers. The code also includes type hints using the function name, parameter, and return. A test case suite is a separate module to run the test cases.