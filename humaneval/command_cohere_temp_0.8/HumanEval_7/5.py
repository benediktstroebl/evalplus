```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the specified substring. It uses a list comprehension, iterating over each string in `strings`, and adding those that include the `substring` to the new list. 

The tests for this function are included in the script and are designed to check its behavior in different scenarios:
```python
def test_filter_by_substring():
    # Empty list, empty substring
    assert filter_by_substring([], 'a') == []

    # List with one element, empty substring
    assert filter_by_substring(['abc'], '') == ['abc']

    # List with one element, non-empty substring
    assert filter_by_substring(['abc'], 'a') == ['abc']

    # List with multiple elements, empty substring
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], '') == ['abc', 'bacd', 'cde', 'array']

    # List with multiple elements, non-empty substring
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

    # List with multiple elements, different substring
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'b') == ['bacd']
```

These tests aim to cover different scenarios, from empty input lists to various types of input lists and substrings, ensuring that the function behaves correctly in each case.