```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, returns the longest one.
    :type strings: List[str]
    """
    if not strings:
        return None
    max_len = max([len(string) for string in strings])
    return strings[0].center(len(strings[0]) - max_len, ' ') + strings[1:]
```
This code defines a function called `longest` that takes a list of strings as input and returns the longest string from the list.

It uses the `max()` function to find the maximum length among the strings in the list, and then subtracts this length from the length of the longest string to center it with the rest of the shorter strings.