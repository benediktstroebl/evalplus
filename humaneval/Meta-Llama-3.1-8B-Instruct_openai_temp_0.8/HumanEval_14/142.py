```python
from typing import List
import itertools

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    :param string: The input string
    :return: A list of all prefixes of the input string
    """
    # Initialize an empty list to store prefixes
    prefixes = []
    
    # Generate all possible prefixes using itertools.imap
    for r in range(1, len(string) + 1):
        for prefix in itertools.imap(lambda x: string[:x], range(1, r + 1)):
            prefixes.append(prefix)
    
    # Sort the prefixes by length
    prefixes.sort(key=len)
    
    return prefixes

# Example usage
if __name__ == "__main__":
    print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that generates all prefixes of a given string, sorts them by length, and returns them as a list. The `itertools.imap` function is used to generate all possible prefixes, and the `sort` method is used to sort the list of prefixes by length.