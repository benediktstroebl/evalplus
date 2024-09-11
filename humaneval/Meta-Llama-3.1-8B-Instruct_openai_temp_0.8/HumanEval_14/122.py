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
    prefixes = []
    for i in range(1, len(string) + 1):
        # Get the prefix of the current length
        prefix = string[:i]
        prefixes.append(prefix)
    return prefixes


# Test the function
print(all_prefixes('abc'))
# Output: ['a', 'ab', 'abc']
```

This script uses a simple loop to generate all prefixes of the input string. For each position `i` from 1 to the length of the string, it extracts the substring from the start to `i` using `string[:i]` and appends it to the list of prefixes. The list is then returned.