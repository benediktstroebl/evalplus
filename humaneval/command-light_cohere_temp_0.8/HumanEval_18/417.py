Here's the self-contained Python function:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string.
    Args: 
    - string: The original string
    - substring: The substring to search for
    Returns: int - Count of occurrences
    """
    return len(string.find(substring))
```

This function takes two parameters: a string and a substring. It then uses the string.s.find() function to find string substring to count the occurrences of the substring in the original string.