```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
    string (str): Input string.

    Returns:
    int: Number of distinct characters in the string.
    """
    # Convert the string to lowercase to ignore case sensitivity
    lowercase_string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set(lowercase_string)
    
    # Return the number of distinct characters
    return len(unique_chars)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```