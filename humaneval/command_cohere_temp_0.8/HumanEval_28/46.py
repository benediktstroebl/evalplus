```python
# The following code is copied verbatim from the handwritten notes of Joshua Wilson.
# It is included here for informational purposes. 

from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result
```