```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): A list of strings to be filtered.
        prefix (str): The prefix that strings should start with to be included in the output.

    Returns:
        List[str]: A list of strings that start with the given prefix.
    """
    # Use a list comprehension to filter the input list
    # The 'if' condition checks if each string starts with the given prefix
    filtered_strings = [string for string in strings if string.startswith(prefix)]
    
    # Return the filtered list of strings
    return filtered_strings

# Test cases
print(filter_by_prefix([], 'a'))
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']
```