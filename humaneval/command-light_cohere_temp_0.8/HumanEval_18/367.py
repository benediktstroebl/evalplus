```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    while ignoring case and handling overlapping correctly.

    """ 
    return sum(1 for _ in string.py.findall(substring,reversed) 
        if substring == "" return 0
    )
```