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
    return [string for string in strings if substring in string]


# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

# Example usage:
if __name__ == "__main__":
    strings_to_filter = ['apple', 'banana', 'orange', 'avocado']
    substring_to_search = 'a'
    filtered_strings = filter_by_substring(strings_to_filter, substring_to_search)
    print(f"Strings containing '{substring_to_search}': {filtered_strings}")
```

This script defines the `filter_by_substring` function as specified, along with example usage and test cases to verify its correctness. The function uses a list comprehension to filter the input list of strings based on the presence of the given substring.