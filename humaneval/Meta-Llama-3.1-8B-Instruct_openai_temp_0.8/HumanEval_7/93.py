```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): The list of strings to filter
    substring (str): The substring to search for

    Returns:
    List[str]: The filtered list of strings
    """
    # Use list comprehension to create a new list that includes only strings containing the substring
    filtered_strings = [string for string in strings if substring in string]
    return filtered_strings

# Example usage:
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script defines the `filter_by_substring` function, which uses a list comprehension to filter the input list of strings based on whether they contain the specified substring. The function then returns this filtered list. The example usage demonstrates how to use the function with the provided test cases.