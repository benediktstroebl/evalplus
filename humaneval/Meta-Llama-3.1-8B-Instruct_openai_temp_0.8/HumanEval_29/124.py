```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The input list of strings.
    prefix (str): The prefix to filter by.

    Returns:
    List[str]: The filtered list of strings.
    """
    # Use list comprehension to filter the list
    # The 'if' condition checks if each string starts with the given prefix
    return [string for string in strings if string.startswith(prefix)]

# Test cases
if __name__ == "__main__":
    assert filter_by_prefix([], 'a') == []
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    print("All test cases pass!")
```

This script meets all the requirements specified. It includes the docstring and comments as requested. The function uses list comprehension to filter the list of strings based on the given prefix. The test cases at the end verify that the function behaves as expected.