```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage:
if __name__ == "__main__":
    input_string = 'abc'
    print(all_prefixes(input_string))
```

This script defines a function `all_prefixes` that generates all prefixes of a given string. It uses a list comprehension to create a list of prefixes by iterating over the length of the string and slicing the string up to each index. The `if __name__ == "__main__":` block demonstrates how to use this function with an example input.