Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_str = max(strings, key=len)
    return longest_str if len(longest_str) == max(len(s) for s in strings) else longest(strings[1:])
```

This script defines a function `longest` that takes a list of strings as input and returns either the longest string in the list or `None` if the list is empty. The function first checks if the list is empty and returns `None` if so. It then finds the longest string in the list using the `max` function with the `key` argument set to the lambda function `len`, which calculates the length of each string. The function returns the longest string if it is the longest in the list, and otherwise, it recursively calls itself on the remaining strings in the list starting from the second element. 

Here is an example usage of the function:
```python
>>> longest(['a', 'bb', 'ccc'])
'ccc'
>>> longest(['abc', 'ab', 'b'])
'abc'
>>> longest(['a', 'a'])
'a'
>>> longest([])
None
``` 

This example demonstrates the function's behavior, including handling lists of varying lengths and handling identical longest strings. 
The function's implementation ensures readability, efficiency, and compatibility with Python's type system using the type annotation `Optional`.