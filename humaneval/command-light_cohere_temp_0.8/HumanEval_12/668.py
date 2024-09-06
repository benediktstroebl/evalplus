Here's the code to solve the task:
```python
from typing import List
def longest(strings: List[str]) -> str:
    # check if empty input list passed
    if not strings:
        return None
    
    # initialize and return first string as longest
    return strings[0]
```
This code is a Python function that aims to find the longest string in a given list. It does this by first checking if the input list is empty. If the list is empty, the function returns None. Otherwise, it returns the string of the first item in the list.