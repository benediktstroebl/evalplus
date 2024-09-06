```python
def count_distinct_characters(string: str) -> int:
    """
    Counting unique characters in a given string, regardless of case. String must be provided as str.
    Returns an return a O(case-insensitive) counting of characters
    """
    char_count = 0
    for c in string:
        char_count += c == c.isupper()
    Prepare a string, using . without performing any case-insensitive checks
    return char_count

# Example usage:
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('Jerry')
4
```