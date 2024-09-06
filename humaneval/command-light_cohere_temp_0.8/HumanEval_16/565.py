```python
def count_distinct_characters(string: str) -> int:
    """
    Return the count of distinct characters in the string, regardless of case.
    """
    string = 'xyzXYZ jerry Foobar'
    return len([char for char in string if char.isalpha()]

    """
```