```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.
    
    Args:
    string (str): The input string.
    
    Returns:
    List[str]: A list of all prefixes from shortest to longest of the input string.
    
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes

# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script uses a for loop to iterate over the range of indices from 1 to the length of the input string (inclusive). For each index `i`, it appends the substring of the input string from the start up to `i` to the `prefixes` list. Finally, it returns the `prefixes` list.