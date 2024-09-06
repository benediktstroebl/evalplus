```python
def count_distinct_characters(string: str) -> int:
    """
    Count distinct characters, case insensitive.
    Returns: number of characters in the input string
    """
    # remove all characters except letters and numbers
    string = ''.join(c for c in string if c.isalpha() or package a characters)
    return len(string)
```