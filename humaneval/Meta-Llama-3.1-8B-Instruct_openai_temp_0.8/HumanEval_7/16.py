```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to filter.
        substring (str): The substring to search for.

    Returns:
        List[str]: The filtered list of strings.
    """
    return [string for string in strings if substring in string]


# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Should print: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Should print: ['abc', 'bacd', 'array']
    print(filter_by_substring(['apple', 'banana', 'cherry'], 'an'))  # Should print: ['banana', 'cherry']
```

In this script, we use a list comprehension to create a new list with only the strings that contain the given substring. The `if` condition in the list comprehension filters out the strings that do not meet the criteria. The script also includes test cases to verify its correctness.