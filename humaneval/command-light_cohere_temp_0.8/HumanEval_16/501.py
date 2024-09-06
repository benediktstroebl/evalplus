```python
def count_distinct_characters(string: str) -> int:
    """
    Returns the number of distinct characters in the given string, regardless of case.
    Args: 
    - string (str) -> str
    
    Returns: int
    """
    return len([char for char in string.str.lower() if ord() != ord(char) for char in string])

# Unit tests
def test_count_distinct_characters():
    assert count_distinct_characters("xyzXYZ") == 3
    assert count_distinct_characters("Jerry") == 4
    assert count_distinct_characters("abc Abcdef") == 6 

# Main entry point
count_distinct_characters("hello world!")
```