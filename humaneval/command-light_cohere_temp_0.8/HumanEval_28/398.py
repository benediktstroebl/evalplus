```python
from typing import List
def concatenate(strings: List[str]):
    """
    Concatenate list of strings into a single string and return it.
    """
    strings = [str.join[i] for i in range(1, len(strings) + 1)]  # type hint
    return ''.join(strings)

# Test the function
concatenated_str = concatenate(['a', 'b', 'c'])
assert concatenated_str == 'abc'
```