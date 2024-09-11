```python
from typing import List


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
    prefixes = []
    for i in range(1, len(string) + 1):
        # slice the string to get all prefixes
        prefixes.append(string[:i])
    return prefixes


# Test the function
print(all_prefixes('abc'))  # ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # ['h', 'he', 'hel', 'hell', 'hello']
```

This Python script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes, from shortest to longest. It uses a for loop to slice the string at each position, effectively generating all prefixes. The function is then tested with two example strings.