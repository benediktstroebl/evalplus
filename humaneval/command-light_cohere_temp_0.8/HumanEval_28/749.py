Here is a self-contained Python script that solves the problem of joining a list of strings into a single string in a markdown code block:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Returns: str - concatenated string
    """
    joined = ''.join(strings)
    return joined
```
The `concatenate` function takes a list of strings as an argument and returns a single string by joining the strings together using the `join` method. The solution is a passed through and meets all the given requirements.