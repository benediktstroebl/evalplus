```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    :param strings: list of strings
    :return: concatenated string
    """
    return ''.join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['abc', 'a']) == 'acb'
if __name__ == "__main__":
    test_concatenate()
```
This code defines the `concatenate` function that takes a list of strings as input and returns the concatenated string. The `test_concatenate` function contains a series of asserts that verify the correctness of the `concatenate` function.