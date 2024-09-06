```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the specified substring. It uses a list comprehension, iterating over each string in `strings`, and including only those strings that have the `substring` present in them. This is denoted by the conditional check `if substring in s` within the list comprehension. 

The function's type hinting also indicates that it returns a list of strings (`List[str]`), and the function signature explicitly specifies that the input parameters are a list of strings (`List[str]`), and a substring (`substring`). 

This solution is robust and efficient, providing a simple and readable approach to filter strings containing a given substring. 

The unit tests for this function are also included, and they correctly demonstrate the behavior of the function with different input combinations of `strings` and `substring`:
```python
def test_filter_by_substring():
    # Empty list, empty substring
    assert filter_by_substring([], '') == []

    # Empty list, non-empty substring
    assert filter_by_substring([], 'a') == []

    # List with one string, empty substring
    assert filter_by_substring(['abc'], '') == ['abc']

    # List with one string, non-empty substring
    assert filter_by_substring(['abc'], 'a') == ['abc']

    # List with multiple strings, empty substring
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], '') == ['abc', 'bacd', 'cde', 'array']

    # List with multiple strings, non-empty substring
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
```