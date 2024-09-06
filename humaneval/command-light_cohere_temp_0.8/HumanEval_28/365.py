```python
from typing import List
def concatenate(strings: List[str]): 
    """ Concatenate list of strings into a single string """
    return ''.join(strings)

# Test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result) # Output: abc

strings = []
result = concatenate(strings)
print(result) # Output: 

strings = [""] * 10 
result = concatenate(strings)
print(result) # Output: 

strings = List([1,2,3])
result = concatenate(strings)
print(result) # Output: 123
```