```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    :type strings: List[str]
    :rtype: str
    """
    return ''.join(strings)

# Testing the function
print(concatenate(['a', 'b', 'c']))  # Expected output: 'abc'
print(concatenate([''])         )  # Expected output: '''
print(concatenate(['a', ' ', 'b'] ))  # Expected output: 'ab'
```
This code provides a self-contained solution to the problem. The function concatenate takes a list of strings as input and returns the concatenated result as a single string. The type of the string is expected to be a string, which is why we are using the join method to concatenate the strings.