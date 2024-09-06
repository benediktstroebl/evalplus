Certainly, here's a self-contained Python function that solves the problem of concatenating strings in Markdown code blocks, along with sample test cases:
```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['---'])
    '---'
    >>> concatenate(['**', 'aa', 'bb', 'ccc'])
    '**aabbccc'
    """
    return "".join(strings)
```
The `concatenate` function takes a list of strings as input and concatenates them into a single string with the HTML-style Markdown code blocks using the `\` prefix and the `""` suffix.