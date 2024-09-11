```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    Parameters:
    string (str): Input string
    Returns:
    List[str]: List of prefixes
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        # Append a substring of string from the start up to i
        prefixes.append(string[:i])
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that generates all prefixes of the input string and returns them as a list. The prefixes are in the order from shortest to longest. The script also includes a test case to demonstrate the function's usage.