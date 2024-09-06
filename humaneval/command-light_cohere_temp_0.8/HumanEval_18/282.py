```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    while ignoring case and not overlapping matches.
    """
    
    # Convert all characters in substring to lowercase to ensure case-insensitive search
    # Use set() to remove duplicate characters from substring
    # Use itertools.join() to split the i'to of each character in substring
    # and count the occurrences in string
    return sum(1 for c in substring if c in string.```? how_many_times is code is:
```