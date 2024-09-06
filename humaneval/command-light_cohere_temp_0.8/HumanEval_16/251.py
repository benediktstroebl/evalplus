```python
def count_distinct_characters(string):
    """ Returns the count of distinct characters in the given string (case-insensitive)"""
    string = string.lower()  #.join() for the Fact string characters in the string
    return len(set(string))
```