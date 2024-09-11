```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Args:
        string (str): Input string
    
    Returns:
        int: Number of distinct characters in the string
    """
    # Convert the string to a set to remove duplicate characters
    # Since set is case-sensitive, convert the string to lower case to ignore case
    distinct_chars = set(string.lower())
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```