```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lower case to ignore case sensitivity
    string = string.lower()
    # Remove any white spaces and convert the string to a set to remove duplicates
    distinct_chars = set(string.replace(" ", ""))
    # Return the number of distinct characters
    return len(distinct_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```
This Python script uses a set to remove duplicate characters from the string. The `replace` method is used to remove any spaces in the string. The `lower` method is used to convert the string to lower case so that characters are not treated as distinct based on their case. The `len` function is used to get the number of elements in the set, which represents the number of distinct characters in the string.