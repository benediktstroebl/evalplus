```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    
    # Use list comprehension to handle any number of inputs
    return ''.join(x for x in strings)
```