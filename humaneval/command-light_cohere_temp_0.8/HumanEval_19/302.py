```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return sorted(numbers) #Call the sort() built-in function to sort the numbers in ascending order.

# Tests suite for sort_numbers() function
def test_sort_numbers():
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers(" eight two three ") == "eight two three"
    assert sort_numbers("nine") == "nine"
    assert sort_numbers("b") == "[]" 
    assert sort_numbers("two") == "two"
    assert sort_numbers("zero") == "[]"
    assert sort_numbers("one") == "one"

if __name__ == "__main__":
    test_sort_numbers()
``` 

The code defines a function called sort_numbers, which takes a space-separated string of numbers from zero to nine as input and returns the string with the numbers sorted in ascending order. The function uses the test suite with several test cases to validate the correctness of the sort_numbers function.