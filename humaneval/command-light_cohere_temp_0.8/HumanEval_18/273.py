```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, 
    without overlapping.
    """
    count = 0
    for i, char in enumerate(string):
        if char == substring: 
            count += 1
        if char == substring[-1] and count > 0: 
            count -= 1  
    return count
```