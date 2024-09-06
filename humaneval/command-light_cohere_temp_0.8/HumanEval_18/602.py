```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring within the original string, considering overlapping substring matches.
    Example: Substring can be a single character or a substring.
    >>> how_many_times('aaa', 'a') # returns 3
    >>> how_many_times('abcdeaaaaaa', 'de') # returns 4
    """
    if len(substring) == 0:  # empty string can never be a substring
        return 0
    
    count = 0
    len_string = len(string)
    
    for i in range(len_string):
        if string[i] == substring: 
            count += 1
    
    return count
```