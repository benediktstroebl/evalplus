```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(''.join(strings)  # type: Union[str, List[str]])
def test_concatenate():
    assert concatenate([], '').strip() == '', "Should get empty string"
    assert concatenate(['a', 'b', 'c']) == 'abc', "Should concatenate correctly"
test_concatenate()
``` 
This script defines a function **`concatenate`** which takes a list of strings and concatenates them into a single string. It also includes a test functions to verify the correctness of the **`concatenate`** function for different inputs.