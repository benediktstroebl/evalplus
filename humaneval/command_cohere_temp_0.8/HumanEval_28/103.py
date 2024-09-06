```python
# Importing the necessary module
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''.join(strings)
    return result
```

This code snippet solves the problem by using the `join` method to concatenate the strings in the provided list into a single string. The `join` method takes an iterable of strings and concatenates them with the specified separator. In this case, since no separator is explicitly given, it will use an empty string `''` as the separator. 

This solution is efficient and provides a clear and concise way to solve the problem.