```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    Args:
        string (str): Input string
    
    Returns:
        List[str]: A list of prefixes in the order from shortest to longest.
    
    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that generates all prefixes of a given string. It uses a for loop to iterate over the string from index 1 to the length of the string, slicing the string up to each index to get each prefix. Finally, it returns the list of prefixes.