```python
from typing import List, Generator

def all_prefixes(string: str) -> List[str]:
    """
    Generate all prefixes of a given string from shortest to longest.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [''.join(s) for i in range(len(string)+1) for s in itertools.combinations(string, i)]

import itertools

# Example usage:
print(all_prefixes('abc'))
```

However it is more efficient to use a list comprehension without itertools:

```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Generate all prefixes of a given string from shortest to longest.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]

# Example usage:
print(all_prefixes('abc'))
```