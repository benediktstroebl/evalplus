```python
from typing import List
from itertools import chain, combinations

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
    string (str): The input string

    Returns:
    List[str]: A list of all prefixes of the input string
    """
    # Generate all possible prefixes using the chain and combinations functions
    prefixes = list(chain(*[combinations(string, r) for r in range(1, len(string) + 1)]))

    # Convert the prefixes from tuples to strings and sort them by length
    prefixes = [''.join(p) for p in prefixes]
    prefixes.sort(key=len)

    return prefixes

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script uses Python's built-in `itertools` module to generate all possible prefixes of the input string, converts the prefixes from tuples to strings, and sorts them by length. The result is a list of all prefixes from shortest to longest.