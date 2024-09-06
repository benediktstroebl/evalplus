```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [''.join(''.join(parts) for parts in string.
    ]
``` 
This code defines a function that takes a string as input and returns a list of all prefixes from shortest to longest. The function uses the string slicing and list comprehension to achieve this.