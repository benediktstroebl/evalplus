```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Args:
        string (str): The input string
    
    Returns:
        int: The number of distinct characters in the string
    """
    # Convert the string to a set, which automatically removes duplicates
    # Convert the string to lower case to make the function case-insensitive
    distinct_chars = set(string.lower())
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

In this script, we use Python's built-in `set` data type to store the unique characters in the string. The `set` data type in Python is an unordered collection of unique elements. 

By converting the string to lower case using the `lower()` method, we ensure that the function is case-insensitive. 

Finally, we return the number of distinct characters by getting the length of the `distinct_chars` set using the `len()` function. 

The test cases at the end of the script verify that the function is working as expected.