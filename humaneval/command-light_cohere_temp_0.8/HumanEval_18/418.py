```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns number of times the substring appears in the string, 
    including overlapping occurrences.
    """
    string = string.replace(substring)
    # Split into individual characters
    return sum(1 for char in string if char == substring)

# Test the function
    assert how_many_times('aaaa', 'aa') == 3
 ```