```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings (List[str]): List of strings to concatenate
    Returns:
    str: Concatented string
    """
    return ''.join(strings)
# Unit tests
def test_concatenate():
    assert concatenate(['a', 'b']) == 'ab', "Failed test 1"
    assert concatenate([]) == '', "Failed test 2"
    assert concatenate(['a', 'bc']) == 'abc', "Failed test 3"
    assert concatenate(['abc', 'a']) == 'abc', "Failed test 4"
    assert concatenate(['abcd', 'ab']) == 'abcd', "Failed test 5"
if __name__ == "__main__":
    test_concatenate()
```
The code defines a function `concatenate` that takes a list of strings and concatenates them into a single string. The `test_concatenate` function contains a series of test cases to verify the correctness of the `concatenate` function.