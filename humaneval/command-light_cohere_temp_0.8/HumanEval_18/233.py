```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the count of occurrences of the substring in the string, 
    ignoring case and also counting overlapping occurrences.
    """
   
    string and substring case-insensensitive.
    """
    how many_many_times('abc', 'cba')
    0
    how_many_times('abc', 'ABC')
    3
    how_many_times('AbC', 'cba')
    2
    """
    # Using string.find() to find the string's substring
    return len(string.find(substring, 0, len(string)))
```