```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of all prefixes of the input string

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Test the function
if __name__ == "__main__":
    print(all_prefixes('abc'))  # ['a', 'ab', 'abc']
    print(all_prefixes('hello'))  # ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, from shortest to longest. The function uses a list comprehension to generate the prefixes, and the `range` function to iterate over the indices of the string. The `[:i+1]` slice is used to get the first `i+1` characters of the string, effectively generating the prefix of length `i+1`.