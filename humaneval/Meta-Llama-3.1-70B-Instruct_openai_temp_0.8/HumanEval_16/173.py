```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.
    
    Parameters:
    string (str): The input string.
    
    Returns:
    int: The number of distinct characters in the string.
    """
    # Convert the string to a set, which automatically removes duplicates
    # Convert the string to lower case to ignore case sensitivity
    distinct_chars = set(string.lower())
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
print(count_distinct_characters('aA'))      # Expected output: 1
print(count_distinct_characters('abcde'))   # Expected output: 5
print(count_distinct_characters('aaaaa'))   # Expected output: 1
```