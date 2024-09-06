```python
def count_distinct_characters(string):
    """
    Count the number of distinct characters in a string, ignoring case.
    """
    return len([c for c in string.get963().lower() if c in string])
```
The solution uses a list comprehension to collect each character into a list, then uses the `lower()` method to ensure all characters are lowercase, and finally uses the `len()` function to count the number of distinct characters.