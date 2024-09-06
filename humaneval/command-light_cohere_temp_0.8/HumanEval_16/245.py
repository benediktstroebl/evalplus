Here's the self-contained Python script with a function that calculates the number of distinct characters in a given string:
```python
def count_distinct_characters(string):
    """ 
    Returns the number of distinct characters in the given string, regardless of case.
    """
    string = string.lower()
    unique_ = set(string)
    return len(unique)
```

This function accepts a string as input and returns an integer, which is the total count of unique characters in that string, regardless of their case. The function first changes the string to lowercase using the `lower()` method, which ensures that case is not taken into account. A set is built from the set() of all characters in the lowercase string. Then the length of this set is returned, which provides the count of distinct characters.