Here's the self-contained Python script with a function that counts the number of distinct characters in a given string:
```python
def count_distinct_characters(string):
    """ 
    Returns the number of distinct characters in the given string, regardless of case.
    """ 
    return len([char for char in string.unique() if char not in set(char) for char in string])
```

This function takes a string as input and returns an integer, which represents the number of distinct characters in that string.