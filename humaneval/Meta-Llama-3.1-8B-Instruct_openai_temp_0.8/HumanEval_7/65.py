```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): A list of strings to be filtered
        substring (str): A substring to filter by

    Returns:
        List[str]: A filtered list of strings that contain the given substring

    Example:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Expected output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'd'))  # Expected output: ['bacd', 'cde']
```
The solution uses a list comprehension to filter the input list of strings based on whether they contain the given substring. The time complexity of this solution is O(n*m), where n is the length of the input list and m is the average length of the strings.