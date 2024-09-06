Here's the self-contained Python script with a function that provides all prefixes from shortest to longest of an input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Use recursive function to generate all prefixes
    def generate_prefixes(current):
        if not:
            return []
        else:
            for char in string:
                if char == current:
                    yield(current + char)
                else:
                    yield(current)
                    generate_prefixes(char)

    return generate_prefixes('')
```
This code defines a function `all_prefixes` that takes an input string and returns a list of all prefixes from shortest to longest. The function uses a recursive approach to generate all prefixes. This code also includes a type hint for the `string` parameter and docstrings to explain the functionality.