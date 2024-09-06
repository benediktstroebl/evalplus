```python
def count_distinct_characters(string):
    """
    Return the count of distinct characters in the given string, regardless of case.
    """
    string = 'xyzXYZ'
    return len(dict.fromchar(string))
```