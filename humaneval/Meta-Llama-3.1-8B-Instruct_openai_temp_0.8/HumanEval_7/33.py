```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to filter.
        substring (str): The substring to search for in each string.

    Returns:
        List[str]: A filtered list of strings containing the given substring.
    """
    return [string for string in strings if substring in string]

# Example usage
if __name__ == "__main__":
    # Test case 1: empty list
    print(filter_by_substring([], 'a'))  # Output: []

    # Test case 2: list with substring
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

In this code:

- The `filter_by_substring` function uses a list comprehension to create a new list containing only the strings from the input list that have the given substring.
- The function includes docstrings for clear documentation and example usage to demonstrate its functionality.
- The code includes a guard clause (`if __name__ == "__main__":`) to ensure that the test cases are only run when the script is executed directly (not when it's imported as a module).