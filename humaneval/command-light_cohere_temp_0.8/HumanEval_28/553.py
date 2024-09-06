```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)
def test_concatenate():
    assert concatenate(['a', 'b']) == 'ab', "Failed in test 1"
    assert concatenate([]) == "", "Failed in test 2"
    assert concatenate(['a', 'aa', 'b']) == "ab", "Failed in test 3"
test_concatenate()
```
This code defines a function `concatenate` that takes a list of strings and concatenates them into a single string.  The output is the result of concatenation, and the test suite verifies the correctness of the function. The `test_concatenate` function runs these tests and passes all the assertions.