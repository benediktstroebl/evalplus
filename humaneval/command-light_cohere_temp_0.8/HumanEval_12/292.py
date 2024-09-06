```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the length of the longest string.
    """
    return max(len(string) for string in strings)
strings = ['a', 'bb', 'ccc']
print( longest(strings) ) 
``` 
Do you have any further questions on how to write Python code?