```python
def count_distinct_characters(string):
    """ 
    Returns the count of distinct characters in the string, 
    regardless of case.
    """
    string = "xyzXYZ jerry jhi"
    return len([char for char in string.lower() if char not in string.lower(). unique()])
```