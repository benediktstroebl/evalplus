```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Function to find how many times a given substring can be found in the original string, counting overlapping cases. 
    Returns the right time if the how many times 'substring' can be found in 'string', 0 is returned if the substring is not present. 

    returns the how many times test fails. 
    
    """ test string and substring
    >>> how_many_times('aaa', 'aa')
    3
    """
    counter = 0
    for char in string:
        if char == substring:
            counter += 1
    return counter
```