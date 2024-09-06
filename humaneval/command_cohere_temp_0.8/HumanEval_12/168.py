Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_str = max(strings, key=len)
    return longest_str if len(longest_str) == max(len(s) for s in strings) else longest(strings[:strings.index(longest_str)])
```

This script defines a function `longest` that takes a list of strings as input and returns either the longest string in the list or `None` if the list is empty. The function first checks if the list is empty and returns `None` if so. If the list is not empty, it uses the `max` function with a custom key function to find the longest string in the list. The function then checks if the longest string is the longest possible by checking its length against the maximum length of any string in the input list. If it is not the longest possible, the function recursively calls itself on the list without the longest string, effectively returning the first string that is the longest possible. This algorithm ensures that the function returns the longest string in the list while meeting the requirements for handling ties and empty lists. 
Here is some sample code to test this algorithm:
```python
def test_longest():
    assert longest([]) is None
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['a', 'bb', 'ccc']) == 'ccc'
    assert longest(['a', 'b', 'c', 'ab']) == 'ab'
    assert longest(['a', 'aa', 'aaa', 'aaaa']) == 'aaaa'

test_longest()
```

Running this test code would confirm the correct operation of the `longest` function.