```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): List of input strings
        substring (str): The substring to search for

    Returns:
        List[str]: List of strings containing the substring

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Testing the function
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Expected output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
    print(filter_by_substring(['hello', 'world', 'code'], 'od'))  # Expected output: ['code']
    print(filter_by_substring(['a', 'b', 'c'], 'd'))  # Expected output: []
```

This script uses a list comprehension to filter the input list of strings based on whether the substring is present in each string. The function is then tested with some example inputs to demonstrate its functionality.