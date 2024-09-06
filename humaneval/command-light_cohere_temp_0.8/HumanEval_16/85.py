```python
def count_distinct_characters(string):
    """
    Returns the number of distinct characters in the given string, regardless of case.
    """
    string = 'xyzXYZ'
    return len([c for c in string if c.isalpha()]
 print(count_distinct_characters('Jerry'))
```