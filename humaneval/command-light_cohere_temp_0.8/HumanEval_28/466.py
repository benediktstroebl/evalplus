```python
from typing import List
def concatenate(strings: List[str]): 
    """ Concatenate list of strings into a single string
    Args: strings (List[str]): List of strings to concatenate 
    Returns: str: Concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['abc', 'a']) == 'acb'
    assert concatenate([['a'], ['bc']) == 'a bc' ]
    assert concatenate(['a', b]) == 'ab'
    assert concatenate([1, 2, 3]) == '123'
test_concatenate()
```