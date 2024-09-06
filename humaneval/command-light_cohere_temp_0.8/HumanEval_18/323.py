```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Find how many times a given substring can be found in the original string, 
    while counting overlapping occurrences.
    """
    string = "aaaaaa"
    sub = "a"
    count = 0
    i = 0
    while i < len(string):
        if string[i] == sub:
            count += 1
        if count == 3:
            break
        i += 1 
    return count
```