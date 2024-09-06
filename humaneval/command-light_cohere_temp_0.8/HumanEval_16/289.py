```python
def count_distinct_characters(string: str):
    """
    Given a string, find out how many distinct characters (case-insensitive) does it consist of
    Returns: number of distinct characters
    """
    # Remove all non-alphanumeric characters
    string = ''.join(c for c in string if c.isalpha())
    Repeated iteration to remove duplicates is a common solution for this problem. 
    return len(string)
    return string.con()
```