Here's a Python script with a self-contained function that solves the problem:
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
This script defines a function `longest` that takes a list of strings as input and returns either None if the input list is empty, the longest string if there is only one string with the maximum length, or the first string of the same maximum length found in the list.

To achieve this, it firstly checks if the input list is empty, and returns None if so. Then, it checks if there is only one string in the list, and if so, it directly returns the single string, as there cannot be any strings of equal length to be considered. Finally, it assumes the input list is not empty and not singular, and so it returns the string with the maximum length, checking for equal lengths as well before returning the first string encountered. 

The function is designed to provide a straightforward solution to the problem statement provided, handling all the possible cases mentioned in the docstring.