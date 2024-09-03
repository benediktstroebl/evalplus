```python
def count_distinct_characters(string: str) -> int:
    """ 
    Count the number of distinct characters in a string while ignoring case.
    
    Args:
        string (str): Input string.
        
    Returns:
        int: Number of distinct characters.
    """
    distinct_characters = set(string.lower())
    return len(distinct_characters)
```