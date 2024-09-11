### Count Distinct Characters in a String
#### Problem Description
The following Python script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, ignoring the case.

```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.

    Example:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters, sets in Python only store unique elements
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

This script uses the `lower()` method to convert the input string to lowercase, and then uses a set to store unique characters. The number of distinct characters is then returned as the length of the set.