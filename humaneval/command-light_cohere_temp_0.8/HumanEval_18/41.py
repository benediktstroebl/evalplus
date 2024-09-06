```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.
    """ using the excellent test and function to count the occurrences of a substring in a string.
    :
    return the count of occurrences
    """
    return len(string.find(substring, string))
```
This function employs the 'find' method from the 'string' module to locate the substring within the original string. 
It returns the count of occurrences, accounting for cases where the substring appears multiple times.