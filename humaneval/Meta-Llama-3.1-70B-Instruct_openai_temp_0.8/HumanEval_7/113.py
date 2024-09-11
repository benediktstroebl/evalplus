```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): Input list of strings.
        substring (str): Substring to filter by.

    Returns:
        List[str]: Filtered list of strings containing the substring.

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
assert filter_by_substring(['hello', 'world'], 'abc') == []
assert filter_by_substring(['substring', 'test_substring_test'],'substring') == ['substring', 'test_substring_test']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that include the given substring. The function uses a list comprehension to achieve this.

The script also includes test cases to verify the function's correctness. The test cases cover various scenarios, including an empty input list, a list with strings containing the substring, and a list with strings not containing the substring.