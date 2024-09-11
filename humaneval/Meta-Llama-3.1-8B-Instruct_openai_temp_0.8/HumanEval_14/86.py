```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of prefixes.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]


# Test the function
if __name__ == "__main__":
    print(all_prefixes('abc'))  # ['a', 'ab', 'abc']
    print(all_prefixes('hello'))  # ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines the `all_prefixes` function, which returns a list of all prefixes of the input string, from shortest to longest. The function uses a list comprehension to generate the prefixes by slicing the input string from index 0 to index `i`, where `i` ranges from 1 to the length of the string. The `if __name__ == "__main__":` block includes example usage of the function.