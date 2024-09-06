Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """
    if not strings:
        return None
    return max(strings, key=len)
```
This code defines a function called `longest` that takes a list of strings as input and returns either the longest string in the list, the first string among those that have the maximum length, or None if the input list is empty. To accomplish this, the code employs the `max` function with a custom key function that specifies the `len` function as the metric for determining the longest string.

Here is an example usage of the function:
```python
>>> longest(['a', 'bb', 'ccc'])
'ccc'
```

And here is an example that tests the function against corner cases:
```python
def test_longest():
    assert longest([]) is None
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
    assert longest(['a', 'b', 'c', 'a']) == 'a'
``` 
This test case covers scenarios such as an empty list, lists with different lengths, and lists with duplicate strings. 

To run these sample tests, you would normally import the `longest` function and then call it with the appropriate inputs. The `assert` statement checks that the output of the `longest` function is correct for each case, and passes the test if the condition evaluates to True. 

Therefore, this code perfectly solves the mentioned problem and the tests demonstrate its correct behaviour.