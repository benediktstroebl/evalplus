```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Function to find how many times a given substring can be found in the original string. 
    Count overlapped cases. 
    Returns: example:
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaaaaa', 'aa')
    2
    """
    counter = 0
    string = string.lower()  # Convert to lowercase to ensure case-insensitive matching
    
    for char in substring: 
        counter += string.find(char) != None
    return counter
```