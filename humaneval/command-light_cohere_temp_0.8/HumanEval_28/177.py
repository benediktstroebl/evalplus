```python
from typing import List
def concatenate(strings: List[str]): 
    return ''.join(strings)

def test_concatenate():
    assert concatenate(['a', 'b']) == 'ab', "Failed to concatenate 'a' and 'b'"
    assert concatenate([]) == "", "Failed to concatenate an empty list"
    assert concatenate(['a', 'b', 'c']) == 'abc', "Failed to concatenate 'abc'"

# Test the function
test_concatenate()
```
This script defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. It also includes a test function to verify the correctness of the `concatenate` function.