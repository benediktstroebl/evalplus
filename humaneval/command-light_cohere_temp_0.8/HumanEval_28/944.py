Here is a Python script with a self-contained function that solves the problem of concatenating strings in Markdown code blocks:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    """
    return ''.join(strings)

def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a', 'bc']) == 'abc'
```

This script defines a function `concatenate` that takes a list of strings and concatenates them into a single string. The `test_concatenate` function contains tests to verify the correctness of the `concatenate` function.