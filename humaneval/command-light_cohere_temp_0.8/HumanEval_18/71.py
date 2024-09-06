```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string, 
    while ignoring case and avoiding overlapping occurrences.
    """
   
    n: int 
    Returns the number of positions where the substring can be found
    """
    return sum(1 for i, x in enumerate(string.find(substring, case=True), count=1)
```