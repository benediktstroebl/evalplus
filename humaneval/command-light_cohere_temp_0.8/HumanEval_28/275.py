```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return "".join(strings)
def test_concatenate():
    assert concatenate([]) == "", "Should return the empty string"
    assert concatenate(['a']) == "a", "Should return the first string"
    assert concatenate(['a', 'b']) == "ab"
    assert concatenate(['a', 'b', 'c']) == "abc"
```
The code defines a function `concatenate` that takes a list of strings as input and returns their concatenation as a single string. It also includes a test_concatenate() function with several assert statements to test the correctness of the `concatenate` function.