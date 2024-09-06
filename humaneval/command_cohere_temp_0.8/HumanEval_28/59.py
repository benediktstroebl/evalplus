```python
# Importing required module
from typing import List


# Define the function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    Empty lists return an empty string.
    """
    result = ''.join(strings)
    return result
```

The following expressions are evaluated as comments in the code:
```
>>> concatenate([])
''
>>> concatenate(['a', 'b', 'c'])
'abc'
```

These expressions confirm that an empty list returns an empty string, and non-empty lists are concatenated element-wise.