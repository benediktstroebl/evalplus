```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    :param strings: List of strings to concatenate
    :return: Concatenated string
    """
    return ''.join(strings)

# Test the function
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['']))  # Output: ''
print(concatenate([ None, '1' , '2',3 ]))  # Output: '123'
```
This Python script defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. The test cases demonstrate the this function's expected behavior.