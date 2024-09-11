```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Convert the string into a set, which automatically removes duplicates
    distinct_chars = set(string)
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

In this code:

- We convert the input string to lowercase to ensure that we're treating 'A' and 'a' as the same character.
- We then convert the string to a set, which removes any duplicate characters. Sets in Python are unordered collections of unique elements.
- Finally, we return the length of the set, which gives us the number of distinct characters in the string.