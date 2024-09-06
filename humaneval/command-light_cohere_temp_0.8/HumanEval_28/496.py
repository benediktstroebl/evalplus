```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate  
    Returns:
        str: Concatenated string 
    """
    return "".join(strings)
def test_concatenate():
    assert concatenate([]) == ""
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate([]) == ""
test_concatenate()
```

The code provides a function called `concatenate` that takes a list of strings as input and returns the concatenated string. The test function passes all tests with the given inputs, and the code is self-contained within this function.