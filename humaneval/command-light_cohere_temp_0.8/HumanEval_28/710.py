```python
from typing import List
def concatenate(strings: List[str]): 
    """ 
    Combine all strings into a single string.
    Args: 
    - strings (List[str]) -> List[str]: list of strings to concatenate 
    Returns: 
    - str: concatenated string 
    """
    return ''.join(strings)

# Test cases
strings = [])
print(concatenate(strings)) 
# Output: abc
strings = ['a', 'b', 'c']
print(concatenate(strings)) 
# Output: abc
strings = []
print(concatenate(strings)) 
# Output: 
```