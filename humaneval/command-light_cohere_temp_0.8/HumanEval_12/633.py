```python
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.

    If list is empty, return None.
    if not strings:
        return None

    longest_str = get_longest(strings)
    return longest_str

def get_longest(strings: List[str]) -> str:
    # Sort the strings
    strings.sort()
    longest_str, _str = "".join()
    for string in strings:
        _str = string.lower()
       
        index = _str.find()  # the index >= 0? str.
    return _ basic.upper()
 longest_str
```