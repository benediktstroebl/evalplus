```python
from typing import List
def concatenate(strings: List[str]): 
    """ 
    Concatenate list of strings into a single string and return it.
    :
    
    :param strings: List[str] (list of strings)
    :return: str (concatenated string)
    """
    return ''.join(strings)

# Unit test
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
```

This code defines a function **`concatenate`** that takes a list of strings as input and concatenates them into a single string, returning the result. It also provides a test cases to ensure the correctness of the function. The output of the function is a space-filled string **`''`** if no input is passed, an individual string if only one input is passed, and the concatenated string if multiple strings are passed.