```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the number of occurrences of the substring in the string, counting overlapping matches. 
    """ 
    Do not split the how_many_times("aaa", "aa")
    Returns 0
    """
    return sum(1 for x in string.find(substring, string))
```