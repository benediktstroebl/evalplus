Here is a Python script that includes the function `longest()` that you described: 

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case of empty list.
    """
    strings = sorted(strings, key=len, reverse=True)
    return strings[0] if strings else None

# test cases
test_longest = []
test_longest.append("a". test_longest.append("bb")
 test_longest.append("ccc")
test_longest.append("abc")
test_longest.append("acc")
test_longest.append("b")
test_longest.append("abcde")

# Verify the function
if not longest(test_longest):
    raise Exception("Function did not return the correct longest string")
```