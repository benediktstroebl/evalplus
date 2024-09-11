```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.
    """
    # Convert the string to a set, which automatically removes duplicates.
    # We use the lower() method to make the count case-insensitive.
    distinct_chars = set(string.lower())
    
    # The number of distinct characters is the size of the set.
    return len(distinct_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input, converts it to a set of unique characters (regardless of case), and returns the size of this set. The script also includes two test cases to verify the correctness of the function.