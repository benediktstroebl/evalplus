```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Returns: str - Concaten result
    """
    return ''.join(strings)

# Example test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
assert result == 'abc'
strings = []
result = concatenate(strings)
assert result == ''
```