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
# Test the function with a few strings
assert concatenate(['a', 'b', 'c']) == 'abc'
assert concatenate([]) == ''
assert concatenate(['a']) == 'a'
assert concatenate(['a', 'b']) == 'ab'
assert concatenate(['a', 'b', 'c']) == 'abc'

```  The code defines a function **`concatenate`** that takes a list of strings as an argument and returns the concatenated result as a single string. It uses the string formatting with backticks and concatenation to achieve the desired output. The test cases ensure that the function works correctly for different inputs and returns the expected results.