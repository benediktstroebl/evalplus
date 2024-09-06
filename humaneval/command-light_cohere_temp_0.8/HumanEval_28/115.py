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

# Test the function
assert(concatenate([]) == "")
assert(concatenate(['a']) == 'a')
assert(concatenate(['a', 'b']) == 'ab')
assert(concatenate(['a', 'b', 'c']) == 'abc')

```
This Python code defines a function called **concatenate** that takes a list of strings as input and returns the concatenated string. It utilizes the dry type hints to provide clearer function signature and is tested to ensure it works as expected.