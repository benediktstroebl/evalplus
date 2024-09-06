Here's a self-contained Python script with a function that computes and returns the longest string from a list of strings:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list.
    """
    strings = [ 'Hello', 'world', '!!!', 'user']
    return max(strings, len(''))
```