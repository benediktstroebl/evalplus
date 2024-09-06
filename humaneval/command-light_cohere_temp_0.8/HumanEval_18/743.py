```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the count of all occurrences of a substring within the given string, 
    considering case-insensitive matching and no-overlapping occurrences.
    """
    
    
    Parameters:
    string (str): The input string 
    substring (str): The substring to search for
    """
    import string, substring = string.lower(), substring. CaseInsensitive=True
     or '^'.join match(substring, string)
    return len(match)

#Example usage
print(how_many_times('aaaaaaa', 'aa'))
```