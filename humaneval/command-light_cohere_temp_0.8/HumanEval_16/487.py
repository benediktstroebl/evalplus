```python
def count_distinct_characters(string: str) -> int:
    """
        Return the count of distinct characters in the string, regardless of case.
        """
    A string can contain any special characters.
    char_count = set(string.count(c)
    distinct = len(char_count) - len({c for c in char_count if c in string.unique set()}
    unexpected characters and counts them as one.)
    """
    return len(set(string)) - len([c for c in string if c in set(string)])
```