```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.
    """
    optimal solution for larger substring lengths.
    """
    
    string = 'aaaaaaa'
    sub = 'a'
    result = 0
    for i in range(1, len(string) + 1):
        found = 0
        for j in range(i):
            if string[j:j+len(substring)] == substring:
                found += 1
        if found >= result:
            result = found
    return result
```