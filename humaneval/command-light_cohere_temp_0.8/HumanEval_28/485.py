Here's the code:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(strings)
# Test case: empty list
test_concatenate([])
# Test case: list of different characters
test_concatenate(['a', 'b', 'c'])
```
This script defines a function `concatenate` that takes a list of strings and returns their concatenation as a single string. It then passes the done using two test cases to ensure the function's correctness.