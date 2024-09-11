```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage
if __name__ == "__main__":
    input_string = 'abc'
    prefixes = all_prefixes(input_string)
    print(f"All prefixes of '{input_string}' are: {prefixes}")
```

This script defines a function `all_prefixes` that uses list comprehension to generate all prefixes of the input string. The function iterates over the length of the input string, creating prefixes by slicing the string up to each index `i+1`. The result is a list of all prefixes, from shortest to longest. The script then includes an example usage of this function in the `if __name__ == "__main__"` block.