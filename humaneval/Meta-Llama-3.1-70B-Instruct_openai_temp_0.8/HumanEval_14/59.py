Here is the Python script that solves the problem:

```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage
if __name__ == "__main__":
    print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script uses a list comprehension to generate all prefixes of the input string. It does this by iterating over the indices of the characters in the string, and slicing the string up to each index + 1 to get all prefixes from shortest to longest.