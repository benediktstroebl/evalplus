### Filter Strings by Substring
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The list of strings to filter.
        substring (str): The substring to search for.

    Returns:
        List[str]: The filtered list of strings.
    """
    return [s for s in strings if substring in s]

# Example usage
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```
This script uses a list comprehension to filter the input list `strings` based on whether each string `s` contains the given `substring`. If a string contains the substring, it is included in the output list.