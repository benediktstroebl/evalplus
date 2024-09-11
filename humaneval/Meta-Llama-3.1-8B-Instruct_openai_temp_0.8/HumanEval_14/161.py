### All Prefixes of a String
#### Python Script

```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.
    
    Args:
        string (str): Input string.
    
    Returns:
        List[str]: List of prefixes in order from shortest to longest.
    
    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

In this script, the `all_prefixes` function uses a list comprehension to generate all prefixes of the input string. The expression `string[:i+1]` generates a substring from the start of the string to the `i+1`-th position, effectively creating a prefix. The `range(len(string))` generates numbers from 0 to the length of the string, which are used to determine the end position of each prefix.