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
    return [string for string in strings if substring in string]


# Example usage
if __name__ == "__main__":
    strings = ['abc', 'bacd', 'cde', 'array']
    substring = 'a'
    filtered_strings = filter_by_substring(strings, substring)
    print(f"Strings containing '{substring}': {filtered_strings}")
    
    # Test cases from the docstring
    empty_list = []
    print(f"Filtered empty list: {filter_by_substring(empty_list, 'a')}")
```

This script defines the `filter_by_substring` function and includes a basic test case in the `if __name__ == "__main__":` block. The function uses a list comprehension to filter the input list of strings and return only the ones that contain the given substring.