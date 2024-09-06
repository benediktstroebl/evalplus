```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string, 
    while ignoring case and without overlapping matches.
    """
    Returns a case-insensitive comparison.
    Returns the string.
    """
    string.count(substring)
   
    """ 
    """
    # Convert to lowercase and remove non-alphanumeric characters
    string = ''.join(char for char in string if char.isalpha())
    string = string.lower()
    result: the number of occurrences of the substring in the original string.
    return string.count(substring)

def test_how_many_times():
    """
    Test the function with various cases.
    """
    # Test with the empty string and a substring
    assert how_many_times("", "") == 0
    
    # Test with one character
    assert how_many_times("aa", "a") == 2
    
    # Test with one character and one substring
    assert how_many_times("aa", "aa") == 3
    
    # Test with longer strings
    assert how_many_times("aaaa", "aa") == 3
    
    # Test with overlapping matches
    assert how_many_times("aaaaaa", "aa") == 4
    
    return 
```