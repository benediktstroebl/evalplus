```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input and returns a new list, `List[str]`, that includes only the strings from the input list that contain the given substring. 

The function utilizes list comprehension with a conditional check, filtering out only the strings that contain the provided substring. 

Such filtering can be useful in various scenarios, like finding specific records in an logs or dataset among many others. 

To test this function, you can use the following unit tests:
```python
def test_filter_by_substring():
    # Test Case: Empty input list
    empty_list = []
    result = filter_by_substring(empty_list, "hello")
    assert result == []

    # Test Case: List with one matching string
    strings = ["hello", "world", "hello, world"]
    result = filter_by_substring(strings, "hello")
    assert result == ["hello", "hello, world"]

    # Test Case: List with multiple matching strings
    strings = ["apple", "orange", "banana", "grape", "apple", "pear"]
    result = filter_by_substring(strings, "apple")
    assert result == ["apple", "apple"]

    # Test Case: List with nested strings
    strings = ["hello", "world", ["hello", "world"]]
    result = filter_by_substring(strings, "hello")
    assert result == ["hello", "hello", ["hello"]]

    # Test Case: Empty substring
    result = filter_by_substring(strings, "")
    assert result == []

test_filter_by_substring()
```

These tests cover different scenarios, including empty input, lists, matching multiple and single strings, and even nested strings.  This helps to ensure that the function is working correctly.  You can run these test cases individually to validate the behavior of the `filter_by_substring` function.  This allows to catch any potential issues before deploying it in a production environment.  As a result, you can feel confident in its reliability.