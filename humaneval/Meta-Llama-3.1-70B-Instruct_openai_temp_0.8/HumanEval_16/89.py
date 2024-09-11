```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string
    """
    # Convert the string to lowercase to ignore case
    lower_string = string.lower()
    
    # Convert the string to a set, which removes duplicates
    distinct_chars = set(lower_string)
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 5
```

This script works by first converting the input string to lowercase to ensure the function is case-insensitive. It then converts the string to a set, which automatically removes any duplicate characters. The number of distinct characters is then calculated by getting the length of the set, which is returned as the result.