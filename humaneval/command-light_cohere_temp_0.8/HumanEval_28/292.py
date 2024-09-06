```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    :param strings: List of strings
    :return: Concatenated string
    """
    return ''.join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
``` 
This code provides a self-contained function `concatenate` that takes a list of strings and returns the concatenated string as a single line. The `test_concatenate` function contains some test cases that verify the correctness of the `concatenate` function.