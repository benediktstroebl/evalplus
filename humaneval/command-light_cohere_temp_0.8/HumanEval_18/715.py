```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count the number of occurrences of a given substring within the original string, 
    accounting for overlapping matches.

    Args: 
    string: str, The input string 
    substring: str, The substring to search for 
    Returns: int, The number of occurrences of the substring
    """
    return len([i for i, match in enumerate(re.search(substring, string)])

# Test function
def test_function() -> None:
    assert how_many_times('Hello', 'world') == 6 # Should return 6
    assert how_many_times('Hello world', 'world') == 6 # Should return 6
    assert how_many_times('Python is awesome!', 'Python') == 3 # Should return 3
```