```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): A list of strings to be filtered
    substring (str): The substring to look for in the strings

    Returns:
    List[str]: A list of strings that contain the given substring
    """
    return [string for string in strings if substring in string]


# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

# Additional test cases to ensure the function works as expected
assert filter_by_substring(['hello', 'world', 'python'], 'hello') == ['hello']
assert filter_by_substring(['apple', 'banana', 'orange'], 'an') == ['banana', 'orange']
assert filter_by_substring(['dog', 'cat', 'bird'], 'bird') == ['bird']
```
This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that include the given substring. It uses a list comprehension to achieve this. The script also includes test cases to verify that the function works correctly.