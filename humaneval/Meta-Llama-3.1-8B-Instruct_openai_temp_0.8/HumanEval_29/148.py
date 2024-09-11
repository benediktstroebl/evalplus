```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): A list of strings to be filtered.
    prefix (str): The prefix to filter the list by.

    Returns:
    List[str]: A list of strings that start with the given prefix.
    """
    # Use list comprehension to filter the list
    # The condition'string.startswith(prefix)' checks if each string starts with the prefix
    filtered_strings = [string for string in strings if string.startswith(prefix)]
    
    return filtered_strings

# Test cases
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # Output: []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It uses list comprehension to achieve this in a concise and efficient manner. The function is then tested with the provided test cases.