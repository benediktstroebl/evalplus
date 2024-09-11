```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.
    
    Args:
        strings (List[str]): The list of strings to be filtered.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: A list of strings that start with the given prefix.
    """
    # Use list comprehension to create a new list containing only strings that start with the prefix
    return [string for string in strings if string.startswith(prefix)]

# Test cases
if __name__ == "__main__":
    assert filter_by_prefix([], 'a') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    print("All test cases pass.")
```

This script defines the `filter_by_prefix` function as specified and includes two test cases to verify its correctness. The `startswith` method is used to check if a string starts with a given prefix. The function uses list comprehension for a concise and efficient implementation.