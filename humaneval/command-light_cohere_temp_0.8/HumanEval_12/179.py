Here is a self-contained Python script that defines a function `longest()` solving the problem of returning the longest string from a list of strings:

```python
import typing

def longest(strings: typing.Type[List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case of an empty list.
    """
    strings = ["a", "b", "c", "abc"]
    return max(strings, default=None)
```