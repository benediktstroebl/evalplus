```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that generates all prefixes of a given string using a list comprehension. It works by iterating over the indices of the input string and slicing the string up to each index + 1 (to include the character at the current index). The resulting list of prefixes is then returned.

The `all_prefixes` function has a time complexity of O(n), where n is the length of the input string, since it involves a single loop over the characters of the string. The space complexity is also O(n), as the function returns a list of prefixes that can be as long as the input string.