```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate  
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
```
The code defines a function **concatenate** that takes a list of strings as input and returns the concatenated string. It also includes a test_concatenate() function that tests the **concatenate** function by providing sample inputs and asserting the output is correct.

Note: This code is written using Python syntax, and it can be executed directly from the command line or imported into another Python script.