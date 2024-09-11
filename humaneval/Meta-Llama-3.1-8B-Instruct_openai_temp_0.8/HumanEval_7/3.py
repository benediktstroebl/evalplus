Here is a Python script that defines the `filter_by_substring` function and includes docstrings and test cases:
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

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]

# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
    print(filter_by_substring(['hello', 'world', 'python'], 'o'))  # ['hello', 'world']
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'x'))  # []
```
This script defines the `filter_by_substring` function using a list comprehension, which filters the input list of strings based on whether each string contains the given substring. The docstring includes a description of the function, its arguments, and its return value, as well as some examples of usage. The script also includes test cases to verify the function's behavior.