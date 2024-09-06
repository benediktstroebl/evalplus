Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        max_idx = strings[0].__len__()
        for string in strings:
            if string.__len__() > max_idx:
                max_idx = string.__len____()
                longest_str = string
        return longest_str
```
The function `longest` works as follows:
1. It validates if the input list is empty and returns `None` if so.
2. When there is only a single string in the list, it returns the lone string.
3. In the case of multiple strings, it identifies the longest one using the `__len__()` method and stores it in the `longest_str` variable.
4. Finally, the function returns the longest string. 

This approach takes advantage of the fact that Python strings themselves have a `__len__()` method that allows us to detect the length of a string without the need for a separate `len` function.