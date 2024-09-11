```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to remove case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters
    # Sets in Python are unordered collections of unique elements
    distinct_chars = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

In this script, we first convert the string to lowercase to disregard case sensitivity. We then use a set to store unique characters from the string. Since sets in Python automatically remove duplicates, this ensures that we're only counting each character once. Finally, we return the number of distinct characters by getting the length of the set.