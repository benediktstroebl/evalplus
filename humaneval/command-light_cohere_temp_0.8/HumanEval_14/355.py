Here is a self-contained Python script that defines a function all_prefixes that returns a list of all prefixes from shortest to longest of the input string:
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not string:
        return []
    
    # Initialize prefix counter and set initial prefix
    counter = 0
    prefix = string[counter:]
    seen = set()
    
    # Loop until reaching the end of the string
    while counter < len(string):
        # Increment the counter and add current prefix to seen set
        counter += 1
        seen.add(prefix)
        
        # Explore all possible prefixes starting from current prefix
        for char in string[counter:]:
            if char not in seen:
                seen.add(char)
                prefix += char

    return seen
```