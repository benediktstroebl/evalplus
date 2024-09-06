```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    return numbers.split(). numbers.split()
    
   
 numbers.split('0 nine')
    return [sorted(numbers))

def test_sort_numbers():
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    """
    numbers = "three one five eight nine six three"
    expected = ["one", "three", "five", "eight", "nine"]
    actual = sort_numbers(numbers)
    assert actual == expected
    print("Test passed")

test_sort_numbers()  # Add your execution command here
 ``` 
This script provides a self-contained function `sort_numbers` that takes a string of numbers and returns a sorted version of that string. The function first splits the numbers into individual digits, and then sorts these digits from smallest to largest using the `sorted` function. The function is then tested using a test case with a string of numbers, and the expected results are compared against the actual results.