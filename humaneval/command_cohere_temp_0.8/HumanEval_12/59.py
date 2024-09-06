Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        max_idx = strings.index(max(strings, key=len))
        return strings[max_idx]
```
This script includes the `longest` function that takes a list of strings (`List[str]`) as input and returns the longest string from the list. If the input list is empty, it returns `None`. If there's only one string in the list, it returns the only string. Finally, if there are multiple strings of the same length, it returns the first one. This function is designed to follow the specified functionality and handle various scenarios. 
Here is a simple test case to ensure the above function works as expected:
```python
def test_longest():
    # Single longest string
    assert longest(['ccc', 'bb', 'a']) == 'ccc'

    # Multiple longest strings
    assert longest(['aa', 'aab', 'abb']) == 'aab'

    # Single string
    assert longest(['a']) == 'a'

    # Empty list
    assert longest([]) is None
``` 
The `test_longest` function provides test cases to cover different scenarios and ensure that the `longest` function behaves as expected. You can use this for testing the function.