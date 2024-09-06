```python
def count_distinct_characters(string):
    """
    Count distinct characters without considering case.
    Return number of characters in the string.
    """
    return len(set(string.lower()))
```