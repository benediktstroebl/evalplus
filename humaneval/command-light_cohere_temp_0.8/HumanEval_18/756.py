```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while ignoring case and overlaps.
    """
   
        same time we're dealing with strings, convert them to lowercase to make the comparison case-insensitive. 
    """
    string = ''.join(string.lower())
    string += substring
    len(string)
    return 1 + len(string)
```