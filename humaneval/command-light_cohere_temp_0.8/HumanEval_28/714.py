Here's a self-contained Python function that performs the task you described:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(strings)
```

This function takes a list of strings as input and returns a single string by concatenating them all together using the `join` method. The function is self-contained, and passes all the tests provided in the problem statement.