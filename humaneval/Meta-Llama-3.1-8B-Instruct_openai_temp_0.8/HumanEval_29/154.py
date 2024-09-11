```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): A list of strings to filter.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: A list of strings that start with the given prefix.
    """
    # Use list comprehension to filter the input list
    filtered_strings = [string for string in strings if string.startswith(prefix)]
    
    # Return the filtered list
    return filtered_strings

# Test cases
if __name__ == "__main__":
    # Test case 1: Empty list
    print(filter_by_prefix([], 'a'))  # Expected output: []

    # Test case 2: Non-empty list
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. The function uses list comprehension to filter the input list in a concise and efficient way. The test cases at the end of the script demonstrate the function's behavior with different inputs.