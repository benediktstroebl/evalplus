```python
def count_distinct_characters(string: str):
    """
    Returns the number of distinct characters in the given string, regardless of case.
    Args: 
    - string (str) - the input string 
    Returns: 
    - int - the number of distinct characters 

     """
    return len([char for char in string.isalpha()])
```