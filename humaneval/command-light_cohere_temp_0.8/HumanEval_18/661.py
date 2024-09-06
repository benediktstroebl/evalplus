```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string, 
    while ignoring case and handling overlaps correctly.
    """
   
    return sum(1 for c in substring if c in string)
    """
    return sum(1 for c in substring if c.lower() in string. lower())
 return 
```
Do you need help with anything else?