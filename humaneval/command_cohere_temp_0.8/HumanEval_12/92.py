```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    return max(set(strings), key=strings.count)
```
This code solves the problem by first checking if the input list is empty. If it is, it returns None according to the specifications of the problem. It iterates over the list of strings and creates a set of unique strings which avoids any potential dups due to ordering and allows us to use the `max` function to retrieve the longest string. It then uses the `count` method to determine the longest string by counting the occurrences of each string in the list and returning the max string. 

Here is the Markdown code block with corresponding tests to ensure the function behaves as expected:
```python
Tests:
>>> longest([], None)
None

>>> longest(["a", "b", "c"], None)
'a'

>>> longest(["a", "bb", "ccc"], None)
'ccc'

>>> longest(["a", "bb", "ccc", "aaaaaa"], None)
'aaaaaa'

>>> longest([], 'default')
'default'

>>> longest(["a", "b", "c"], 'default')
'a'

>>> longest(["a", "bb", "ccc"], 'default')
'ccc'

>>> longest(["a", "bb", "ccc", "aaaaaa"], 'default')
'aaaaaa'
```