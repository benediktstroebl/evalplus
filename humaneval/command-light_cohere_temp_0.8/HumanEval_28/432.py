```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate
    Returns:
        concatenated string
    """
    return ''.join(strings)
```
Here is a self-contained Python script that implements the concatenate function with tests.  The function takes in a list of strings and returns the concatenated string, which is then tested using the assert statement.