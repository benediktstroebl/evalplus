```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate
    Returns:
        concatenated string
    """
    return "".join(strings)

# Test the function
concatenated_str = concatenate([])
# Should return an empty string """
print(concatenated_str)

concatenated_str = concatenate(['a', 'b', 'c'])
# Should return the string 'abc'
print(concatenated_str)
```