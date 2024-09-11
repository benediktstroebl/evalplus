```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Example usage
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Expected output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
```

This script uses a list comprehension to create a new list containing only the strings from the input list that contain the given substring. The `in` operator is used to check if a substring is present in a string. The script also includes example usage in the `if __name__ == "__main__":` block to demonstrate how to use the `filter_by_substring` function.