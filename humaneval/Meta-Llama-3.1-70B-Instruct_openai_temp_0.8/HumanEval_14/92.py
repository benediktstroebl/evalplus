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
if __name__ == "__main__":
    print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
    print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that generates all prefixes of a given string, from shortest to longest. It uses a list comprehension to create the list of prefixes, slicing the input string up to each index `i+1` (since indexing starts at 0). The example usage demonstrates how to use this function with the provided test case and an additional example.