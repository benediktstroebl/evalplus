```markdown
### List of All Prefixes of a String

This Python script generates a list of all prefixes from the shortest to the longest of a given input string.

```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage
print(all_prefixes('abc'))
```

### Output
```python
['a', 'ab', 'abc']
```

### Explanation

This script uses a list comprehension to generate all prefixes of the input string. It iterates over the string using the `range(len(string))` function, where `i` is the index of the current character. The prefix up to the current index `i` is obtained using `string[:i+1]`. The `+1` is necessary to include the current character in the prefix. The resulting list of prefixes is returned by the function.