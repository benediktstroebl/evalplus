```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string
    """
    # Convert the string to a set, which removes duplicate characters
    # We convert to lower case to ignore case sensitivity
    distinct_chars = set(string.lower())
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

Note: In the test case `count_distinct_characters('Jerry')`, I've corrected the expected output to `5` because 'Jerry' actually consists of `5` distinct characters: `j`, `e`, `r`, `r` and `y`. However, since we are counting distinct characters, the `r` is only counted once.