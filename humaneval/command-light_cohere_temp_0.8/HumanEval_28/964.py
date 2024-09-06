```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    :param strings: list of strings to concatenate
    :return: concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
# test cases
test_concatenate()
```
The above Python script defines a function `concatenate` that takes a list of strings as input and concatenates them into a single string. It also includes a test cases that verify the correctness of the `concatenate` function.