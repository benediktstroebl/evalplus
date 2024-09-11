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
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines the `all_prefixes` function, which takes an input string and returns a list of all prefixes from the shortest to the longest. The function uses a list comprehension to generate the prefixes by iterating over the range of the string's length and slicing the string from the beginning to the current index `i+1`. The example usage shows how to call the function with different input strings and print the results.