```markdown
### Distinct Characters Counter

This Python script defines a function `count_distinct_characters` which takes a string as input and returns the number of distinct characters in the string, ignoring case.

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
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set(string)
    
    # Return the number of unique characters
    return len(unique_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

### Explanation

*   The function `count_distinct_characters` takes a string as input and converts it to lowercase using the `lower()` method to ignore case sensitivity.
*   It uses a set (`unique_chars`) to store unique characters from the string. Sets in Python automatically eliminate duplicate values.
*   Finally, it returns the number of unique characters by getting the length of the set with `len(unique_chars)`.
*   The function includes docstrings with examples to demonstrate its usage and expected output.

You can run this script to test the function with different inputs.