```python
def count_distinct_characters(string: str) -> int:
    """
    Returns the count of distinct characters in the string regardless of case.
    """
    ensure all input is a string, we will convert it to lowercase to make character comparison case-insensitive.
    return the Read
    using set() and list() we can easily filter out duplicates and get unique characters.
    return count of distinct characters
   
    """
    return len(set(string.lower()))
```