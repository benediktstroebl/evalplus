Here's the self-contained Python function that finds the number of times a given substring can be found in the original string, while accounting for case and overlap:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    while handling case-sensitive and ignoring overlap.
    """
    unique index for each character in the substring and original string are returned.
    """
    
    Parameters:
    string (str): the original string
    substring (sub): the substring to search for
    """
    sub = sub.lower()  # for char in substring: string = string.replace(char, string)
    index = string.find(sub)
    if index == -1: return 0
    return 1 + how_many_times(string, sub[index:])
```