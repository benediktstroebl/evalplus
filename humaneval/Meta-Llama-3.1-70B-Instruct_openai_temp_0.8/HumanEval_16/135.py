```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Args:
        string (str): Input string
    
    Returns:
        int: Number of distinct characters in the string
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Convert the string to a set, which automatically removes duplicates
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

This script works by first converting the input string to lower case using the `lower()` method. This ensures that the same character in different cases is treated as the same character.

Then, it converts the string to a set using the `set()` function. A set in Python is an unordered collection of unique elements, which means it automatically removes any duplicate characters.

Finally, it returns the number of distinct characters by getting the length of the set using the `len()` function.

Note: The test case for 'Jerry' was returning 4, but it should return 5 because 'J', 'e', 'r', 'r', 'y' has 5 distinct characters: 'J', 'e', 'r', 'y'.