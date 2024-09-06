```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string Count overlapping cases.

    # Split string and 
    # convert to lowercase to ensure case-insensitive matching
    string = string.str.lower()
   baum

    how many with substring
    total = 0
    for char in string:
        if char == substring:
            total += 1
    return total
```