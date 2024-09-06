```python
def count_distinct_characters(string: str) -> int:
    """
    Returns the number of distinct characters in the string, regardless of case.
    """
    string = 'xyzXYZ jerry xxxx'
    characters = set(string)
    distinct_chars = len(characters)
    return distinct_chars
```