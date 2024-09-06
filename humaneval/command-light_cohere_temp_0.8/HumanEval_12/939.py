```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Find the length of the longest string in the list.
    """
    strings = [string for string in strings if string]
    return max(strings, key=len)
``` 
The function `longest` takes a list of strings as an argument. It creates a specific list of strings that are in the input list but are also in the list. Then, the function uses the max function with the `key=len` argument to find the length of the longest string in the list.