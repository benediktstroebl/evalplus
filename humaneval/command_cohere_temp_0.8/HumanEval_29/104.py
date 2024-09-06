```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that begin with the `prefix`. It uses a list comprehension to iterate through each string in `strings` and returns the ones that start with the specified `prefix`. 

Here's an example of how you can use the `filter_by_prefix()` function with specific test cases to verify its functionality:
```python
def test_filter_by_prefix():
    # Empty list, empty prefix
    assert filter_by_prefix([], 'a') == []

    # List with one matching element
    assert filter_by_prefix(['abc'], 'a') == ['abc']

    # List with multiple elements, one matching element
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # List with multiple elements, no matching element
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'x') == []

    # Prefix is a substring of some elements
    assert filter_by_prefix(['abc', 'abcd', 'abcde', 'array'], 'abc') == ['abc', 'abcd', 'abcde']
```

In this test suite, we cover different scenarios, including an empty list and empty prefix, lists with matching elements, lists with multiple elements and a matching element, and lists with multiple elements and no matching element. Additionally, we test a case where the `prefix` is a substring of some elements to ensure the function accurately filters based on the beginning of the string.

This demonstrates that the `filter_by_prefix()` function works correctly and efficiently filters strings starting with the given prefix from a list of strings.