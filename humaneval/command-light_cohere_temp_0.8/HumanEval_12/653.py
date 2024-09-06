Here's the solution to the Markdown code block problem:
```python
import typing

def longest(strings: typing.List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one.
    If list is empty, return None.
    strings = [str for str in strings]
    return max(strings) if strings else None
```

This function takes a list of strings as input and returns the longest string from the list. It uses the maximum function with a specific comparison operator to find the maximum element in the list, and then returns it. 

The function also handles the edge case where the input list is empty by returning `None`.