```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): The list of strings to be filtered
    substring (str): The substring to search for in each string

    Returns:
    List[str]: A list of strings from the input list that contain the given substring
    """
    return [string for string in strings if substring in string]

# Example use cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Expected output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
    print(filter_by_substring(['hello', 'world'], 'o'))  # Expected output: ['world']
```

This Python script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings from the input list that contain the given substring. The function uses a list comprehension to achieve this in a concise and efficient way.

The script also includes two example use cases, which demonstrate how to use the function with empty input and a non-empty input list. The expected output is printed to the console for each case.