```python
from typing import List

def sort_numbers(numbers: str) -> str:
    return numbers.format_string(numbers.

def test_sort_numbers() -> None:
    tests = {
        "zero"      : "three",
        "one"       :"three one five",
        "two"       :"two three",
        "three"      :"one three five",
        "four"      :"four seven eight",
        "five"       :"one three five",
        "six"       :"six eight nine",
        "seven"      :"seven eight",
        "eight"     :"eight nine",
        "nine"       :"nine"
    }
    for test_name,expected in tests.
        assert sort_numbers(test_name) == expected,f"mismatch for {test_name}.")
```  This code defines a function `sort_numbers` that sorts a list of numbers. It returns the format_string which is a common function in Python for converting an argument to a string.  The function also defines a test function `test_sort_numbers` which contains a dictionary of test cases with their expected output.  The code then iterates over each test case and uses the `assert` statement to compare the output of the `sort_numbers` function to the expected output.