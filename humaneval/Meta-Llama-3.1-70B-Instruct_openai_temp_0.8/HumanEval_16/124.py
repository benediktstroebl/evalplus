```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
    string (str): The input string.

    Returns:
    int: The number of distinct characters in the string.
    """
    # Convert the string to a set of unique characters (case-insensitive)
    unique_chars = set(string.casefold())
    
    # Return the number of unique characters
    return len(unique_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, regardless of case. The function uses Python's built-in `set` data structure to create a set of unique characters from the input string, and then returns the size of this set. The `casefold()` method is used to convert the string to a case-insensitive format before creating the set of unique characters. The script also includes two test cases to demonstrate the usage of the function.