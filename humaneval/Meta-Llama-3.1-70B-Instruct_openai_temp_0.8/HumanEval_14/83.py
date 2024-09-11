```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
if __name__ == "__main__":
    input_string = 'abc'
    prefixes = all_prefixes(input_string)
    print(prefixes)  # Output: ['a', 'ab', 'abc']
```

In this script, we define a function `all_prefixes` that takes an input string and returns a list of all its prefixes from shortest to longest. We use list comprehension to generate the prefixes. The `string[:i+1]` expression is used to extract substrings from the input string, starting from the first character up to the `i-th` character. The range of `i` goes from 0 to `len(string) - 1`, thus covering all prefixes of the input string.