```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the input prefix. It uses a list comprehension to iterate through each string in the input list and checks if it starts with the specified prefix using the `startswith` method. If a string starts with the prefix, it is included in the resulting list. If it does not, it is excluded from the list. 

This solution passes the given tests because:
- If the input list is empty, the function returns an empty list.
- If the input list contains 'abc', 'bcd', 'cde', 'array', and the prefix is 'a', the function returns ['abc', 'array']. 

These expectations are specified in the function's docstring, which reflects the problem statement and test cases. 

This code is concise, efficient, and easy to understand, making it a good solution for the problem. 

It can be tested directly in the Python interpreter:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'arr')
['array']
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'xyz')
[]
``` 
```python
def test_filter_by_prefix():
    # Empty list, empty result
    assert filter_by_prefix([], 'a') == []

    # List with matching strings, filtered list
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # List with one matching string, filtered list
    assert filter_by_prefix(['abc'], 'a') == ['abc']

    # List with multiple matching strings, filtered list
    assert filter_by_prefix(['abc', 'abd', 'abz'], 'ab') == ['abc', 'abd', 'abz']

    # Non-matching prefix, empty result
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'xyz') == []
``` 

This way, the code adheres to the principle of separation of concerns, making each part of the code focused on individual responsibilities, enhancing its maintainability.