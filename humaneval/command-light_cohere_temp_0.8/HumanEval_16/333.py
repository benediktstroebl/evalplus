Here's the corrected version of the Python script with a self-contained function that counts the distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    """
    Counts the number of distinct characters in the given string, regardless of case.
    Args:
    string (str): The input string
    Returns:
    int: Number of distinct characters
"""
    return len([char for char in string.get().lower() if char != ''])
```