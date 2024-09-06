```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the given prefix. The function uses a list comprehension, `return_list = [string for string in strings if string.startswith(prefix)]`, to iterate over each string in the input list and check if it starts with the specified prefix. If it does, the string is included in the resulting list. If it doesn't, the string is excluded. 

The function's type annotation, `def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:`, indicates that it takes a list of strings and a string as input and returns a list of strings. The functionality of the function is further demonstrated by the following tests:
```python
def test_filter_by_prefix():
    # Basic test for the filter_by_prefix function
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ar') == ['array']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'non-existent') == []

def test_filter_by_prefix_empty_list():
    # Test for an empty list
    assert filter_by_prefix([], 'a') == []

def test_filter_by_prefix_nonexistent_prefix():
    # Test for a non-existent prefix
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'x') == []

``` 

These tests cover different scenarios, including existing and non-existent prefixes for filtering and testing with both empty and non-empty input lists. 
To further improve the function, an additional test could be added to ensure that the function handles the case where the prefix is a string of multiple characters. 

Let me know if I can help with anything else!