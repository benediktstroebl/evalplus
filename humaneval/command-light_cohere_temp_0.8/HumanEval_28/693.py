```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string """
    return ''.join(''.join(strings))

#Test cases
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b', 'c']) == 'abc'

if __name__ == "__main__":
    test_concatenate()
```
This code defines a function called `concatenate` that takes a list of strings as input and returns the concatenated string. The test_concatenate function passes all the test cases, which are written to cover the expected behavior of the `concatenate` function.