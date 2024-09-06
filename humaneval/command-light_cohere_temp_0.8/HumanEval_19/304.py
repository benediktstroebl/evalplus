```python
from typing import List

def sort_numbers(numbers: str) -> str:
    return numbers.

# Unit tests
def test_sort_numbers():
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("six four three") == "four three six"
    assert sort_numbers("nine eight seven six") == "eight seven six nine"
    assert sort_numbers("Ten Ice Tea") == "Ten Ice Tea"
    assert sort_numbers("zero nine eight seven six") == "zero eight seven six nine"
    assert sort_numbers(" Seven eleven ") == "seven eleven"

# The main function to call tests
test_sort_numbers()
``` 
This Python script defines a function sort_numbers that takes a string of numbers as input and returns the string with numbers sorted from smallest to largest. The script also includes unit tests for the function to ensure its correctness.