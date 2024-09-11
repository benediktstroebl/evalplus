```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
    string (str): The input string

    Returns:
    int: The number of distinct characters in the string
    """
    # Convert the string to lowercase to ignore case differences
    string = string.lower()
    
    # Convert the string to a set to remove duplicates
    distinct_chars = set(string)
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

In this script, the function `count_distinct_characters` takes a string as input and returns the number of distinct characters in the string, ignoring case. The script uses Python's built-in `set` data structure to remove duplicates from the string, and the `len` function to get the number of elements in the set.