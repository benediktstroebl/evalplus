```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.
    """
    # Convert the string to a set, which removes duplicates, and to lower case to ignore case sensitivity
    distinct_chars = set(string.lower())
    # Return the number of distinct characters
    return len(distinct_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 5
```

In this script, we define a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, regardless of case. We use the built-in `set` data structure to remove duplicates from the string, and the `lower` method to convert the string to lower case to ignore case sensitivity. Finally, we use the `len` function to get the number of distinct characters.

The script also includes two test cases to demonstrate how the function works.