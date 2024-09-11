```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
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
    
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters
    unique_characters = set()
    
    # Iterate over each character in the string
    for char in lower_case_string:
        # Add the character to the set
        unique_characters.add(char)
    
    # The number of distinct characters is the size of the set
    return len(unique_characters)


# Test the function
print(count_distinct_characters('xyzXYZ'))
print(count_distinct_characters('Jerry'))
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string (regardless of case). It uses a set to store unique characters and returns the size of the set as the result. The script also includes example use cases and test cases to demonstrate its usage.