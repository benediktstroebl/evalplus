```python
def count_distinct_characters(string: str) -> int:
    """
    Returns the count of distinct characters in the string, regardless of case.
    """

    The character set is converted to lowercase to ensure all characters are treated as distinct
    """
    set(string.ascii()) | set()
    unique = len(set(string))
    return int(unique)
```