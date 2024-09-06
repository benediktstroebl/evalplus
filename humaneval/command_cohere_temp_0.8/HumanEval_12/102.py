```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    return max(strings, key=len)
```
This Python script defines a function called longest in the code above that takes a list of strings, initials function parameters, and returns the longest string from the list. If the list is empty, it returns None. If there's only one string in the list, it returns that string. If there are multiple strings of the same length, it returns the first one. Otherwise, it returns the longest string using the max function with the length of the string as the key. 
This approach ensures that the function handles various scenarios and returns the longest string or an appropriate None value. Picking the first string in case of ties avoids complexity and provides a simple and efficient solution. 
The function is well-typed, using the List and Optional types from the typing module to ensure type-safety and proper handling of input and output types.