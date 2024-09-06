```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate
    Returns:
        concatenated string
    """
    return ''.join(strings)
# Test case 1: empty list
test_concatenate([])
# Test case 2: list of single character strings
test_concatenate(['a'])
# Test case 3: mixed list of strings
test_concatenate(['a', 'b', 'c'])
```
The code defines a function called `concatenate` which takes a list of strings as input and returns the concatenated string. It utilizes the`**. common approach of joining the list using an `append` operation to a single string. The test cases demonstrate how the single character strings and mixed strings can be concatenated correctly.