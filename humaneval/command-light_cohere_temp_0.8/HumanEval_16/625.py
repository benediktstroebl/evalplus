```python
def count_distinct_characters(string):
    """
    Given a string, find out how many distinct characters (case-insensitive) does it consist of. {
    
    return len([c for c in string.upper if c not in string.lower()])

    """ simple case, just counts the number of unique characters regardless of case.

"""
# Testing
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('jerry'))  # Output: 4
```