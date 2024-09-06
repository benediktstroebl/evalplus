Here is a self-contained Python script that defines a function to count the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in the given string, ignoring case.
    Returns the count of distinct characters in the given string.
    """
    string = 'XYZ abcDefg12345%'
    return len(set(string))
```