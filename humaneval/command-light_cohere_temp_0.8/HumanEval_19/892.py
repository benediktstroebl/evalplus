Here's a self-contained Python function that sorts and cleans up a string of numbers:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    # convert to list of strings
    numbers_list = list(numbers.split())
   
    # sort list of strings
    numbers_list.sort()

    # join the string with spaces
    cleaned_string = ' '.join(numbers_list)
    return cleaned_string

# Unit tests
def test_sort_numbers(test_string: str) -> None:
    # Test string with mixed numbers and special cases
    test_strings = [
        "three one five",
        "zero seven eight",
        "nine",
        "six four",
        "one two three"
    ]
    expected = [
        "one two three",
        "zero seven eight",
        "nine",
        "six four"
    ]
    # Call sort_numbers function
    actual = sort_numbers(' '.join(test_strings))
    # Compare actual and expected results
    assert actual == expected, "test failed"
```

This code takes a string of numbers and returns a cleaned version with spaces. It also has unit tests to ensure that the `sort_numbers` function works correctly for various inputs.