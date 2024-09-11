```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of all prefixes of the input string
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

In this script, we use a list comprehension to generate all prefixes of the input string. The expression `string[:i+1]` gets the substring from the start of the string up to the character at index `i+1` (since Python's slicing is exclusive of the end index). We iterate over all indices in the string using `range(len(string))`, and add 1 to the index to include the character at that index in the prefix.