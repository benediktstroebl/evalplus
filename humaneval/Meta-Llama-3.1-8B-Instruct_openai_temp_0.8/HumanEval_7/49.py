```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The input list of strings
        substring (str): The substring to search for

    Returns:
        List[str]: A list of strings that contain the substring
    """
    return [string for string in strings if substring in string]


# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
    print(filter_by_substring(['hello', 'world', 'python'], 'o'))  # ['hello', 'world']
    print(filter_by_substring(['apple', 'banana', 'cherry'], 'x'))  # []
```

This script defines the `filter_by_substring` function, which uses a list comprehension to filter the input list of strings and return a new list containing only the strings that contain the given substring. The test cases demonstrate its usage with different inputs.