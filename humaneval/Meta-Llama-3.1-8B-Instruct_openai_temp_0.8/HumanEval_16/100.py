```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Args:
    string (str): The input string
    
    Returns:
    int: The count of distinct characters in the string
    """
    
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Convert the string to a set, which automatically removes duplicates
    distinct_chars = set(string)
    
    # Return the count of distinct characters
    return len(distinct_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

This script uses the `set` data structure in Python, which is an unordered collection of unique elements. By converting the string to a set, we automatically remove duplicates and get a collection of distinct characters. The `len` function is then used to get the count of these distinct characters. The test cases at the end demonstrate the function's usage and expected output.