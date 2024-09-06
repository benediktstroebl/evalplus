```python
from typing import List
def concatenate(strings: List[str]): 
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        string
    """
    return ''.join(strings)

# Test the function with sample inputs and expected outputs
strings = ['a', 'b', 'c']
result = concatenate(strings)
assert result == 'abc'
```