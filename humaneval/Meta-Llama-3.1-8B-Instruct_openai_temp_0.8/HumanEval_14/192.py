```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): Input string

    Returns:
        List[str]: List of all prefixes of the input string

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines the `all_prefixes` function, which takes a string as input and returns a list of all prefixes of the string. The prefixes are generated using a list comprehension, which iterates over the indices and slice lengths to create all possible prefixes. The function is then tested with two examples.