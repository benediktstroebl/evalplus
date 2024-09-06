```python
def count_distinct_characters(string: str):
    """
    Returns the number of distinct characters in the given string, regardless of case.
    Args: 
        string (str): The input string
    Returns: 
        int: Number of distinct characters
    """
    return len(set(string.lower()))
```