```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the number of times the substring can be find 
    in the original string.
    """ 
    return sum(1 for i,x in enumerate(string.find(substring)))
```