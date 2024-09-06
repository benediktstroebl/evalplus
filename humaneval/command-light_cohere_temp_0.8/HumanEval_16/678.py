Here is a self-contained Python function that finds the count of distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a string, ignoring case.
    """
    return len([c for c in string. characters() if c.isupper() and distinct() 
    ```
```

This function uses a list comprehension to filter out all characters that are not unique from the string, and then returns the length of this list.