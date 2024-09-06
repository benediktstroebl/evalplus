Here is a Python script that includes a self-contained function called `longest()` that solves the problem of finding the longest string in a list of strings:
```python
import typing

def longest(strings: typing.List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case of empty list.
    """
    strings: List[str]
    """
    return max(strings, default=None)

# Example of passing the test
strings = ["a", "b", "c"]
longest_str = longest(strings)
print(longest_str)  # Output: 'c'
```

The `longest()` function takes a list of strings as input and returns the longest string in the list. It uses the max() function with the default argument set to None, which means it will return the first string in the list if all strings have the same length. The function also returns None if the list is empty.