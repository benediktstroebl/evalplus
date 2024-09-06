```python
from typing import List
def concatenate(strings: List[str]): 
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate  
    Returns: 
        concatenated string
    """
    return ''.join(strings)
# Example test case
test_concat = [
    "", "a", "bc"
]
assert concatenate(test_concat) == "abc"
```