```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string Count overlapping cases."""
    
    return sum(1 for i,x in enumerate(string.find(substring in string) or i == 0)
```