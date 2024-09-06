```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate
    Returns:
        string
    """
    return ''.join(strings)
#Test cases
print(concatenate([]))  # Output: ''
print(concatenate(['a']*3))  # Output: 'aaa'
print(concatenate(['a', 'b']*2))  # Output: 'ababb'
print(concatenate(['a', 'bcde']))  # Output: 'abcde'
print(concatenate(['a', 'bcdef', 'acefg']))  # Output: 'abcdefg'
```
This Python script defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. It is tested with various test cases, which demonstrate the correctness of the `concatenate` function.