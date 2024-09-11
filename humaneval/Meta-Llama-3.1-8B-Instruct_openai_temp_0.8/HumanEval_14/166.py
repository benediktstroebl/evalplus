```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of all prefixes of the input string, from shortest to longest
    """
    # Use list comprehension to generate all prefixes and sort them by length
    return sorted([string[:i+1] for i in range(len(string))])

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of that string, sorted from shortest to longest. The function uses list comprehension to generate all prefixes, and the `sorted` function to sort them by length. The script also includes some test cases to demonstrate the function's behavior.