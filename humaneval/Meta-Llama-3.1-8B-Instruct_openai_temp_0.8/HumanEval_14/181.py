```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of prefixes in order from shortest to longest

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

In this code:

- We define a function `all_prefixes` that takes a string `string` as input.
- We use a for loop to generate all prefixes of the string. We start the loop from 1 (to generate the first character) and end at the length of the string plus one (to include the entire string). Inside the loop, we append the first `i` characters of the string to the `prefixes` list.
- Finally, we return the `prefixes` list.
- We test the function with the input `'abc'` and print the result.