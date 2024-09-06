```python
def count_distinct_characters(string):
    """
    Returns the number of distinct characters in the string (case insensitive).
    """
    return len({char for char in string.characters()})
in 'xyzXYZ'
        3
        4
```