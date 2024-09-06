```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input and returns a new list containing only the strings from the input list that contain the given substring. This algorithm uses a list comprehension, creating a new list by applying a conditional check to each element in the input `list`. The conditional check employs the in operator to determine if the `substring` is present in each `string` in the list, an essential technique for searching strings within strings in Python. The expression `substring in string` returns True if the `substring` is found within the `string`, and False otherwise. The list comprehension constructs a new list that includes only those `strings` for which the condition is `True`, meaning those strings that contain the specified `substring`. 

The provided example tests below demonstrate the functionality of the function using specific test cases:
```python
def test_filter_by_substring():
    # Empty list, empty substring
    assert filter_by_substring([], '') == []

    # List with one matching string
    assert filter_by_substring(['abc'], 'a') == ['abc']

    # List with multiple matching strings
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

    # List with no matching strings
    assert filter_by_substring(['pizza', 'pasta', 'burger'], 'soup') == []

test_filter_by_substring()
```

These tests check for the function's behavior in different scenarios, including empty lists, lists with matching strings, lists with multiple matching strings, and lists with no matching strings.