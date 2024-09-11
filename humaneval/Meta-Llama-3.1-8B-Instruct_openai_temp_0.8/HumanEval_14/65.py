```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
        string (str): Input string
    
    Returns:
        List[str]: List of prefixes in the order from shortest to longest
    
    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = [string[:i+1] for i in range(len(string))]
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines the `all_prefixes` function, which takes a string as input and generates a list of all prefixes of that string. The function uses a list comprehension to create the list of prefixes. The outer loop iterates over the indices of the string, and the inner expression `string[:i+1]` extracts the prefix of length `i+1` (since indices are 0-based, we use `i+1` to get the correct length). The function then returns the list of prefixes.

Finally, the script tests the `all_prefixes` function with two example calls.