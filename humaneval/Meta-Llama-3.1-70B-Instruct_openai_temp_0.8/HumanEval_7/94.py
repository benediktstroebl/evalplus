```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The input list of strings.
        substring (str): The substring to filter by.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
assert filter_by_substring(['hello world', 'world cup', 'python'], 'world') == ['hello world', 'world cup']
```

This script defines a function `filter_by_substring` that uses list comprehension to filter the input list of strings. The function returns a new list containing only the strings that contain the given substring.

The script includes test cases to verify the correctness of the function. The test cases use the `assert` statement to check that the function returns the expected output for different inputs.