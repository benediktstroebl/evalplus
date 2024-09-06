```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping matches.
    """ string = string.
    substring = substring
   
    count = 0
    i = 0
    while i < len(string):
        if string[i] == substring: 
            count += 1
        i += 1
    return count
```