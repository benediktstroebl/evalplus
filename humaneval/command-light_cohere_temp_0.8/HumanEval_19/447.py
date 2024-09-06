```python
from typing import List

def sort_numbers(numbers: str) -> str:
    return numbers. Spaces are delimited and all uppercase letters are removed. All valid choices are numbers are converted to strings. After that, a list comprehension is used to sort the numbers string. The sorted list is then converted back to a string.

tests = {
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
}

for test_case in tests:
    actual_output = sort_numbers(test_case)
    assert actual_output == test_case

print("All tests passed!")
```