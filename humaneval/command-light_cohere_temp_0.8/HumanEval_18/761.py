Here is a self-contained Python script that solves the problem of finding how many times a given substring can be found in the original string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.
    """ The many the time is O(n)
    where n = len(string)
    and s is of length m.
    """
    string = str.strip(string)
   
    string = ''.join(string)
    return sum(1 for i in range(len(substring)) if string[i:i+len(substring)] == substring)
```