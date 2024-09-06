Here is a self-contained Python function that finds the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    """ 
    Count the number of distinct characters in the given string, 
    regardless of case. 
    Returns: number of unique characters 
    """
    return len({c for c in string if c.isalpha() and})
```