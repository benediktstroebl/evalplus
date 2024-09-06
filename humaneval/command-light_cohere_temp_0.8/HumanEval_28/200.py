```python
from typing import List
def concatenate(strings: List[str]): 
    """ Concatenate list of strings into a single string """
    return ''.join(strings)
# test case
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result) # expected output: abc
```