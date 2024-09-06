Here is a self-contained Python script that solves the problem of sorting numbers in markdown code blocks:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are number strings are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split(" ").
    list(map(lambda x: int(x)-1, numbers)))
    .sort()
    .join(" ")

# Example test cases
test_sort_numbers = """
def test_sort_numbers():
    assert sort_numbers("three one five") == "one three five"

def test_empty_string():
    assert sort_numbers("") == ""

def test_mixed_numbers():
    assert sort_numbers("8 six 7") == "eight six seven"

def test_negative_numbers():
    assert sort_numbers("-6") == "six"

def test_infinitely_long_numbers():
    assert sort_numbers("a") == "a"

def test_space_delimited():
    assert sort_numbers("three one five") == "one three five"

def test_mixed_separators():
    assert sort_numbers("three one five nine") == "one three five nine"
"""
``` 
This script defines a function sort_numbers that sorts a string of numbers. It also provides a test cases for various scenarios, such as empty strings, mixed numbers, negative numbers, infinitely long numbers, space-delimited strings, and mixed separators.