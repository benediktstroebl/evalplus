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

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```
In this script, we use list comprehension to generate all prefixes of the input string. The expression `string[:i+1]` generates the prefix of the string up to the `i-th` index (inclusive), and we iterate over all indices in the string to generate all prefixes.