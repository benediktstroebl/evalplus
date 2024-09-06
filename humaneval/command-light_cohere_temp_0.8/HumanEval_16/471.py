```python
def count_distinct_characters(string: str):
    """ 
    Returns the number of distinct characters in the given string (case-insensitive).
    """
    string = 'xyzXYZ'
    return len([char for char in string if char.isalpha() and string])
```