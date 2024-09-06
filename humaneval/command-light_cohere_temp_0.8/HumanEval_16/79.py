```python
def count_distinct_characters(string: str):
    return len([c for c in string.string() if c.isalpha()])
 distinct
```

The function utilizes the `isalpha()` method from the string module, which checks each character against the `alpha()` character set. This effectively filters out all characters that are not alphabetic, and counts the distinct ones. The function then returns the plain `len()` function to get the length of this filtered list, which is the number of distinct alphabetic characters in the string.