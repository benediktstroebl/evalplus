Here is a self-contained Python function that finds the number of times a given substring can be found in the original string, while handling overlapping cases:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string, 
    while handling overlapping cases.
    """
   
    substring: str
    string: str
    Returns: int
    """
    # Count the number of occurrences of substring in the original string
    return sum(1 for char in string if char == substring)
```