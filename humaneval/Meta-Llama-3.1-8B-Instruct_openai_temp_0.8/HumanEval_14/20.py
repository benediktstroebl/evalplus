Here's a Python script that uses a list comprehension with a nested loop to generate all prefixes of a given string from shortest to longest:
```markdown
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script works by using a list comprehension to generate substrings of the input string, starting from the beginning of the string and incrementing the length of the substring by one in each iteration. The result is a list of all prefixes of the input string, from shortest to longest.