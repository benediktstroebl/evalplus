```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
    string (str): The input string.

    Returns:
    int: The number of distinct characters in the string.
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters. Sets in Python automatically eliminate duplicates.
    unique_chars = set(lower_case_string)
    
    # Return the number of unique characters, which is the size of the set.
    return len(unique_chars)

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 5
```

This script works by first converting the input string to lower case, so that the same character in different cases is not counted as distinct. Then, it uses a set to store the characters in the string. Sets in Python automatically eliminate duplicates, so this ensures that each character is only counted once. Finally, it returns the number of unique characters, which is the size of the set.