Here is a self-contained Python script that solves the problem of concatenating strings in Markdown code blocks: 

```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)
```