```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
        string (str): The input string
    
    Returns:
        List[str]: A list of all prefixes of the input string
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script uses a list comprehension to generate all prefixes of the input string. The `string[:i+1]` expression slices the string up to the `i+1` index, effectively generating all prefixes from the shortest to the longest. The `range(len(string))` expression generates indices from 0 to the length of the string minus 1, allowing us to generate all prefixes.

You can run this script as is, and it will output `['a', 'ab', 'abc']` when given the input `'abc'`.