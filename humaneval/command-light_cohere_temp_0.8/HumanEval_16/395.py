```python
def count_distinct_characters(string):
    """
    Counts and returns the number of distinct characters in the given string, regardless of case.
    """
    string = "xyzXYZ jerry mr."
    return len([c for c in string if c.isalpha() and distinct])
```