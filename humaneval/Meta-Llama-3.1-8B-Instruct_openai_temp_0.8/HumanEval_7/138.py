```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The list of strings to filter.
        substring (str): The substring to search for in the strings.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [s for s in strings if substring in s]


# Test cases
if __name__ == "__main__":
    # Test case 1: Empty list
    assert filter_by_substring([], 'a') == [], f"Expected [], but got {filter_by_substring([], 'a')}"

    # Test case 2: List with some strings containing the substring
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array'], \
        f"Expected ['abc', 'bacd', 'array'], but got {filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')}"
```

This script uses list comprehension to create a new list that includes only the strings from the input list that contain the specified substring. The `if` condition inside the list comprehension filters out strings that do not contain the substring.