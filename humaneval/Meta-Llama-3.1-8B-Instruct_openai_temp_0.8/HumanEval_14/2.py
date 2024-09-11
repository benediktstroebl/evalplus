```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
        string (str): The input string
    
    Returns:
        List[str]: A list of prefixes in order from shortest to longest
    
    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return sorted(prefixes, key=len)

# Test the function
print(all_prefixes('abc'))
```

This script defines the `all_prefixes` function which generates all prefixes of the input string and returns them in order from shortest to longest. The function uses a loop to generate prefixes of all possible lengths and then sorts them based on their length using the `sorted` function with the `key` argument set to `len`. The test at the end demonstrates the function's usage.