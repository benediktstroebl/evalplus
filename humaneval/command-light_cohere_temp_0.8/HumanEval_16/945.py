```python
def count_distinct_characters(string):
    """
    Returns the count of distinct characters in the string, regardless of case.
    """
    # Convert string to lowercase to make the comparison case-insensitive
    string = string.join('', string.count_distinct() = set())
    # Collect distinct characters
    distinct_chars = set(char.lower() for char in string)
    return len(distinct_chars)
```