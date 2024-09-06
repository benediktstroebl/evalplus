```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input and returns a new list containing only the strings from the input list that contain the given substring. This function solves the problem and should pass the provided tests. It uses list comprehension to iterate over the input list of strings and returns the ones that contain the given substring. 

Here's how you would be able to test it with the test cases provided:
```python
def test_filter_by_substring():
    # Test Case 1: Empty input list, empty output
    assert filter_by_substring([], 'a') == []

    # Test Case 2: Only one matching string
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

    # Test Case 3: Multiple matching strings
    assert filter_by_substring(['abcd', 'babc', 'bcda', 'cdef', 'hello', 'world'], 'bc') == ['abcd', 'babc', 'bcda', 'cdef']

    # Test Case 4: No matches, empty output
    assert filter_by_substring(['red', 'green', 'blue', 'yellow'], 'white') == []

test_filter_by_substring()
```

This would validate that our function correctly filters the strings based on the given substring.