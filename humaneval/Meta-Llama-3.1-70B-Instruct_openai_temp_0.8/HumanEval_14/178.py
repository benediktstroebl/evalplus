```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
        string (str): The input string.
    
    Returns:
        List[str]: A list of all prefixes from shortest to longest.
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script uses a list comprehension to generate all prefixes of the input string. It iterates over the string indices and slices the string up to each index, effectively creating all prefixes. The prefixes are then returned as a list.