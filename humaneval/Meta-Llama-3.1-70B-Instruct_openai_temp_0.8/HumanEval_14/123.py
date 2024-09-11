```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return a list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

In this script, we define the `all_prefixes` function, which uses list comprehension to generate a list of all prefixes of the input string. The `string[:i+1]` expression slices the string up to the current index `i+1`, effectively creating a prefix of the original string. We iterate over the indices of the string using `range(len(string))` to generate all prefixes. The function returns this list of prefixes.