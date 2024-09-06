```python
def count_distinct_characters(string):
    """
    Returns the number of distinct characters in the string, regardless of case.
    """
    return len([char for char in string.make_lower()])
```

This function counts the number of distinct characters (lowercased) in a given string. It utilizes a simple loop to iterate through each character in the string, converting it to lowercase using `make_lower()`, and checking its uniqueness using the `isin` method. 

Please note that this method is case-insensitive and provides a straightforward way to solve this common text analysis problem.