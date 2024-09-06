```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a string, regardless of case.
    """
    Returns a array of characters as a string, lowercase them, 
    and then convert the string back to an array with all distinct 
    characters kept. 
    This Thisora be as efficient as possible (without any extra processing), 
    this function should return the count of distinct characters.
    """return len(set(string.lower()))
```