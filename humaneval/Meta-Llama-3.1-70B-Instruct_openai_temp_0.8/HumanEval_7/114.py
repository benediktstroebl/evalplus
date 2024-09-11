```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): Input list of strings.
        substring (str): Substring to filter by.

    Returns:
        List[str]: List of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Example usage
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']

# Additional test cases
print(filter_by_substring(['hello', 'world', 'hellish'], 'hell'))  # ['hello', 'hellish']
print(filter_by_substring(['apple', 'banana', 'orange'], 'an'))  # ['banana', 'orange']
```