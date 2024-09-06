```python
def count_distinct_characters(string):
    """
    Return the number of distinct characters in the given string, regardless of case.
    """
    string = "xyzXYZ jerry jones dory"
    return len([char for char in string.get(), ""])
 distinct_characters = sum(1 for c in string if c.isalpha() and ord() not in set(c))
```