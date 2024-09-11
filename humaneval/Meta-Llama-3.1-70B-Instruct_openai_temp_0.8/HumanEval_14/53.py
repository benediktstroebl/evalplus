```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script uses a list comprehension to generate all prefixes of the input string. It iterates over the indices of the string and uses slicing (`string[:i+1]`) to get the prefix up to the current index. The result is a list of all prefixes from shortest to longest.

You can save this script to a file (e.g., `prefixes.py`) and run it using Python (e.g., `python prefixes.py`). The example usage at the end demonstrates how to call the `all_prefixes` function and print its output.