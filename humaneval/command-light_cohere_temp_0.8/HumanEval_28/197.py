Here is a Python script with a self-contained function that solves the problem of concatenating strings in Markdown code blocks:

```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string with proper markdown code entities.
    >>> 
    >>> [['**' ,'**]']
    '****'
    """
    return ''.join(strings)
```