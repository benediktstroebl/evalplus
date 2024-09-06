```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return "".join(strings)

def test_concatenate() -> None:
    assert concatenate([]) == ""
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
This code defines a function `concatenate` that takes a list of strings and returns a concatenated version of those strings. It then defines a test_concatenate function with the purpose of testing the `concatenate` function.