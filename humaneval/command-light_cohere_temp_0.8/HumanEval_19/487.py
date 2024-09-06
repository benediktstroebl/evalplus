```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split()
    hangs with numbers sorted from smallest to largest
    """ <start of test cases> 

test_valid_input()
    assert sort_numbers("three one five") == "one three five"
   

test_invalid_input()
    assert sort_numbers("hello") == ""
   
test_empty_input()
    assert sort_numbers("") == ""

test_duplicate_numbers()
    assert sort_numbers("four five six seven") == "five six seven"

test_invalid_chars()
    assert sort_numbers("a1 three five") == "1 three five"

<end of test cases>