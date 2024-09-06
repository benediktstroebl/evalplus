```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        return max(strings, key=len)
```
This Python script defines a function called longest in the code above that takes a list of strings, which is the parameter named strings. It returns the longest string from this list, based on the length of each string. If the list of strings is empty, it returns None. If the list has only one item, it returns that string, regardless of its length. But if there is more than one string, it returns the longest one by using the max function and specifying the key argument to be the len function, which calculates the length of each string.