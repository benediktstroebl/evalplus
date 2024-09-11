```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
        string (str): The input string
    
    Returns:
        List[str]: A list of all prefixes of the input string
    
    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Expected output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Expected output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that generates all prefixes from the shortest to the longest for a given string. It does this by iterating over the string, starting from the second character (index 1) up to the last character (index `len(string)`). At each iteration, it appends the substring from the start of the string to the current index to the `prefixes` list. The function returns the list of prefixes.