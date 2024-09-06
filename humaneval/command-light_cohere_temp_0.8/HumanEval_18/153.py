```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns number of occurrences of substring in string.
    Args: 
        - string: The input string 
        - substring: The substring to find
    Returns: The number of occurrences of substring in string
    """
    return len(string.find(substring))
```
The function uses the 'find()' function to find the occurrences of the given substring in the string.