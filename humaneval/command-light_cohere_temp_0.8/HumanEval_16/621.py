```python
def count_distinct_characters(string: str):
    """
    Returns the number of distinct characters in the given string, regardless of case.
    """
    string = 'xyzXYZ jerry jule'
    return len([c for c in string if c.isalpha() andnot in string.isalpha()])

""" 
    > string = 'xyzXYZ jerry jule'
    > result = count_distinct_characters(string)
    print(result)  # Output: 6
```