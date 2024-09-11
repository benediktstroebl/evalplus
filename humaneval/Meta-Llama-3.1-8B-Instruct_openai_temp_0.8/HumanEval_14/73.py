```markdown
## All Prefixes of a String

This Python script generates all prefixes of a given input string, from shortest to longest.

### Code

```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """Return list of all prefixes from shortest to longest of the input string

    Args:
    string (str): The input string.

    Returns:
    List[str]: A list of all prefixes of the input string.

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]
```

### Usage

You can use this function to generate all prefixes of a string by passing the string as an argument.

```python
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

### Explanation

This script uses a list comprehension to generate all prefixes of the input string. The expression `string[:i+1]` returns a slice of the string from the beginning to the `i+1`-th character, effectively creating a prefix of the string. The `range(len(string))` function generates a sequence of indices from 0 to the length of the string, and the list comprehension iterates over this sequence to create the list of prefixes.