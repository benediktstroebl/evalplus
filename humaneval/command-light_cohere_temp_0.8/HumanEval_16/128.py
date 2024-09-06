```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a string, regardless of case.
    """
    return len(set(char for char in string.unique())
"""
    This function utilizes Python's built-in `set` and `len` functions to efficiently count the distinct characters in a given string.