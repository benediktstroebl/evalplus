```python
from typing import List
import itertools


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of all prefixes in the input string, from shortest to longest

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    # Use itertools chain and combinations to generate all prefixes
    prefixes = [''.join(p) for r in range(1, len(string) + 1)
                for p in itertools.combinations(string, r)]
    
    # Filter to include only strings
    prefixes = [p for p in prefixes if isinstance(p, str)]
    
    # Sort the prefixes in ascending order of length
    prefixes.sort(key=len)
    
    return prefixes


# Test the function
print(all_prefixes('abc'))
```

This script defines the `all_prefixes` function, which generates all prefixes of the input string using itertools. It then sorts these prefixes by length and returns the result. The example test case at the end demonstrates the function's behavior.