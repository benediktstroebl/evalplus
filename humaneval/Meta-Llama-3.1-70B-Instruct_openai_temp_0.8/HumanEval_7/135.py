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

if __name__ == "__main__":
    print("All test cases passed.")
```

This script uses a list comprehension to filter the input list of strings. It checks if the given substring is present in each string and includes it in the output list if it is. The test cases at the end ensure the function behaves correctly.