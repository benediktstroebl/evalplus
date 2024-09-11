```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The list of strings to filter.
        substring (str): The substring to search for in the strings.

    Returns:
        List[str]: A new list containing only the strings that contain the substring.
    """
    return [string for string in strings if substring in string]


# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
assert filter_by_substring(['hello', 'world'], 'goodbye') == []
assert filter_by_substring(['python', 'java', 'c++'], 'java') == ['java']
assert filter_by_substring(['apple', 'banana', 'orange'], 'an') == ['banana', 'orange']
```