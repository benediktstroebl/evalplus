```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string. 
    Returns the worst instance of this function:
    > how_many_times('aaa', 'a')
    3
    """
    count = 0
    start = 0
    end = len(string) - 1
    while start <= end:
        count += string[start:end] == substring
        start += 1
    return count
```