```python
def count_distinct_characters(string: str) -> int:
    """
    Returns the number of distinct characters in the given string, regardless of case.
    """
    string = "xyzXYZ abcDef"
    return len(string.find(c for c in string if c.isalpha())

    """
    """ Test case 1 """
    assert count_distinct_characters("xyzXYZ") == 3

    """ Test case 2 """
    assert count_distinct_characters("Jerry") == 4

    """ Test case 3 """
    assert count_distinct_characters("ABC123") == 3

    """ Test case 4 """
    assert count_distinct_characters("jerry") == 3

    return  # This is a comment and also signals the end of function definition
```
Do this code solve the problem?