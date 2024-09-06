```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.sort_to_string(numbers)  # sorting numbers to string format
    """
    numbers = numbers.split(' ')')
    sort_to_string(numbers)
    return sort_to_string(numbers)

def sort_to_string(numbers: List[str]) -> str:
    """Return the string with numbers sorted from smallest to largest"""
    numbers = [int(num) for num in numbers]
    numbers.sort()
   	   return ' '.join(str(num) for num in numbers)

def test_sort_numbers() -> None:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    input_str = 'three one five'
    assert sort_numbers(input_str) == 'one three five'
``` 
The code implements the sort_numbers function that takes a string of space-separated numbers as input, which represents a sequence of numbers from smallest to largest. It then converts the rights these input into a list of integers, sorts it, and converts it back into a string format. The sort_to_string function is used to create the string representation of the sorted numbers. The test_sort_numbers function takes an input string and asserts that the sort_numbers function returns the correct sorted string.