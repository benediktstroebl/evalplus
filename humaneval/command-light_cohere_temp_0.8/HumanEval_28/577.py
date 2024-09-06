```python
from typing import List
def concatenate(strings: List[str]):
    """
    Concatenate list of strings into a single string
    :param strings: List of strings
    :return: String
    """
    return ''.join(strings)

# Test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)  # Output: abc

strings = []
result = concatenate(strings)
print(result)  # Output: 

strings = ["a", "bc"]
result = concatenate(strings)
print(result)  # Output: abc

strings = ["abc", "de"]
result = concatenate(strings)
print(result)  # Output: de
```