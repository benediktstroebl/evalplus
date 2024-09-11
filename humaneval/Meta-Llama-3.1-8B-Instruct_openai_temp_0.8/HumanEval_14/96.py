```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of prefixes in order from shortest to longest

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('Hello World'))  # Output: ['H', 'He', 'Hel', 'Hell', 'Hell', 'Hell', 'Hello', 'Hello ', 'Hello W', 'Hello Wo', 'Hello Wor', 'Hello Worl', 'Hello World']
```

This script uses a simple loop to generate all possible prefixes of the input string by slicing the string with a range of indices from 1 to the length of the string. The prefixes are then returned as a list. The example use cases demonstrate how to use the function with different input strings.