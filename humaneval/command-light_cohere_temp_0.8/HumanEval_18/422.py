Here is a self-contained Python function that finds the number of times a given substring can be found in the original string, while also handling overlapping cases:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while handling overlaps.
    """
    
    # Check if the string contains the substring
    if substring in string:
        return 1
    
    # Count how many times the substring can be found
    count = 0
    start, end = substring, substring
    while start <= string.find(end):
        count += 1
        start += end[0] - start
    return count
```