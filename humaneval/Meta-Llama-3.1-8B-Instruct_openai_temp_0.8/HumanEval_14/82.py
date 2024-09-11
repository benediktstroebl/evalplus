```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.
    
    Args:
        string (str): The input string.
    
    Returns:
        List[str]: A list of all prefixes of the input string.
    
    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script uses a list comprehension to generate all prefixes of the input string. The outer loop `range(len(string))` iterates over the indices of the string, and for each index `i`, the inner `[string[:i+1]]` generates a slice of the string up to `i+1`. This slice is a prefix of the original string and is appended to the list. The resulting list is then returned.