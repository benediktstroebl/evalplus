```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = [int(x) for x in numbers.
    numbers.sort()
   ac
    ** string containing the numbers sorted from smallest to largest
    """
    numbers = [int(x) for x in numbers]
    numbers.sort()
    string containing numbers sorted from smallest to largest.

def test_sort_numbers():
    """
    Test the sort_numbers function
    """
    # Example input string
    input_string = """three one five"""

    # Call the sort_numbers function
    result = sort_numbers(input_string)

    # Compare the result to the expected output
    expected = """one three five"""
    assert result == expected
    print("Test passed!")
test_sort_numbers()  # This line will print "Test passed" if the test passes.