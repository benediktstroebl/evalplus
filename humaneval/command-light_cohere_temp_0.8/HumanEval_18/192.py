```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, taking overlapping cases into account. 
    >>> string: The input is the original string
    >>> substring: The input is the substring to search for
    >>> return: The function returns the number of occurrences of the substring in the original string, considering case-insensitive and overlapping matches.
    """
    
    #Examples example:
    >>> how_many_times('aaa', 'aa')
    3
    >>> how_many_times('abcdeabcba', 'abc')
    3
    >>> how_many_times('abcdaa', 'abcd')
    3
    """
    
    # Count occurrences of the substring using set data structure
    occurrences = set()
    for char in substring:
        occurrences.add(string.find(char))
    
    return len(occurrences)
```