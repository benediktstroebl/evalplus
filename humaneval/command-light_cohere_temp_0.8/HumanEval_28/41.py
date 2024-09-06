```python
from typing import List
def concatenate(strings: List[str]):
    """
    Concatenate list of strings into a single string and return the result
    :param strings: list of strings
    :return: concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == '', 'empty list should return empty string'
    assert concatenate(['a']) == 'a', 'single string should be returned'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
```
The function concatenate, which takes a list of strings as input and returns the concatenated string, is implemented in this Python code. The test_concatenate function contains some test cases that check the correctness of the concatenate function. The test passes all test cases, confirming that the function works as expected.