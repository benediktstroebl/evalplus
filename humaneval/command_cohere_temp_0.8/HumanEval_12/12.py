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
This Python script defines a function called longest in the code above that takes a list of strings, lists the words in the text, and returns the longest string in the list of inputs. If the list is empty, the function returns None. If the list only contains strings of the same length, it returns the first one. Otherwise, it returns the longest string in the list using the max function, specifying the length of the string as the key. This ensures the longest string is returned from the list of strings passed into the function.