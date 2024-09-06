```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a string regardless of case.
    Args: 
        string (str): A string
    
    Returns: 
        int: Number of distinct characters in the string
    """
    import re
    return len(re.findall(char for char in string.findall(char.lower() if char in string))
```