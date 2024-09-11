```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    
    Args:
        string (str): The input string
    
    Returns:
        List[str]: A list of all prefixes of the input string, from shortest to longest
    
    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Test the function
if __name__ == "__main__":
    print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
    print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

In this script, we use a list comprehension to generate all prefixes of the input string. The expression `string[:i+1]` generates a substring of `string` from the start to the `i+1`th character, effectively creating all prefixes of `string`. The `range(len(string))` function generates numbers from 0 to `len(string) - 1`, which correspond to the indices of the characters in `string`.