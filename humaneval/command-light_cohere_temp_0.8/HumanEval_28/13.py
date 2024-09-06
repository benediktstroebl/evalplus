Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
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
# Test the function with sample inputs and assert the output
assert concatenate(['a', 'b', 'c']) == 'abc'
```
This script defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. The test case at the time is that the function is tested with the sample input of ['a', 'b', 'c'], and the assertion is `assert concatenate(['a', 'b', 'c']) == 'abc'` is passed, which ensures the correctness of the function.