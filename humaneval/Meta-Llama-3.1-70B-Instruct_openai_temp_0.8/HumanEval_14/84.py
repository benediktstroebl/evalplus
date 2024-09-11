```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']

# Test case
assert all_prefixes('abc') == ['a', 'ab', 'abc'], f"Expected all_prefixes('abc') to return ['a', 'ab', 'abc'] but got {all_prefixes('abc')}"
```

In this script, the `all_prefixes` function uses a list comprehension to generate all prefixes of the input string. The `string[:i+1]` expression slices the string from the beginning up to the `i+1`-th character, effectively creating a prefix of length `i+1`. The `range(len(string))` generates indices from 0 up to the length of the string minus 1, allowing us to create prefixes of all possible lengths.