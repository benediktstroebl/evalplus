```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to filter.
        substring (str): A substring to filter by.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
assert filter_by_substring(['hello', 'world', 'python'], 'o') == ['world', 'python']
assert filter_by_substring(['apple', 'banana', 'cherry'], 'x') == []
```

In this script, we define the `filter_by_substring` function that takes a list of strings and a substring as input. It uses a list comprehension to filter the input list and returns a new list containing only the strings that include the given substring. We also include test cases to verify the correctness of the function.