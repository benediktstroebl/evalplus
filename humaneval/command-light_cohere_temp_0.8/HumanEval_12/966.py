Here is a self-contained Python function that solves the problem you provided:
```python
def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    
    # Sort the strings alphabetically
    strings.sort()
    strings = [c for c in strings if c != ''] + [c for c in strings if c]
    return max(strings, key=len)
```
This function takes a list of strings as input and returns the longest string in the list. The function first checks if the strings list is empty, and if so, it returns None. If the list is not empty, the function sorts the strings alphabetically and then uses the max function with the key `len` to find the longest string. The result is the same as in the provided code.