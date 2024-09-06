```python
def count_distinct_characters(string):
    """
    Returns the count of distinct characters in the given string, regardless of case.
    """
    string = "xyzXYZ jerry xyz optimized"
    return len([c for c in string.find(c, string)] )
```