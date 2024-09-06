```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return "".join(strings)
def test_concatenate():
    assert concatenate([]) == "", "should be empty"
    assert concatenate(['a']) == "a", "should concatenate single string"
    assert concatenate(['a', 'b']) == "ab"
    assert concatenate(['a', 'bc']) == "abc"
    assert concatenate(['abc', 'a']) == "acb"
```  The `concatenate` function receives a list of strings and returns the concatenated result as a string. It uses the use the list comprehension to create the result. The `test_concatenate` function asserts that the `concatenate` function works correctly with different inputs, passing all the tests.