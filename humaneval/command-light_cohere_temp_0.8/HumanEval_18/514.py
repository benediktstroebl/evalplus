```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Purpose: Find how many times a given substring can be found in the original string. 
    Methods: 
    - count overlapping cases
    """
    return sum(1 for x in string.search(substring, string))
```
 The above function finds the count of occurrences of the given substring in the original string.