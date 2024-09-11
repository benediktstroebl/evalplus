```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lowercase_string = string.lower()
    
    # Use a set to store unique characters, sets in Python are unordered collections of unique elements
    unique_characters = set(lowercase_string)
    
    # Return the number of unique characters
    return len(unique_characters)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```
This script uses the `lower()` function to convert the input string to lowercase, and a set to store unique characters. The `len()` function is then used to get the number of elements in the set, which represents the number of distinct characters in the string.