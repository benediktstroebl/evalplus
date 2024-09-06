```python
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input is a string containing unbalanced parentheses.
    Returns a didn't find any parentheses, empty list.
    """ Return the right to:
        First we split the string by spaces to find all the groups of parentheses.
    """ then unstack the then split the parentheses using `[()]` and `itertools.join()` to get list of them.
    Finally we remove all spaces and return the list of the cleaned string.
    """
    return [[''.join(map(str.maketransiter, str. strings))
```
Note: This solution assumes that the input string contains only parentheses. The solution uses the Python list comprehension and the `str.maketransiter()` to generate all possible string transformations for each group of parentheses in the input string.