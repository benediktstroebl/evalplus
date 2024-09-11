### Count Distinct Characters in a String

```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
    string (str): The input string

    Returns:
    int: The number of distinct characters in the string

    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case differences
    lowercase_string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set(lowercase_string)
    
    # Return the number of unique characters, which is the size of the set
    return len(unique_chars)

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This script uses a set to efficiently store unique characters in the string. Sets in Python are unordered collections of unique elements, making them ideal for this task. The `len()` function is then used to get the number of unique characters, which is the size of the set. The script also handles case differences by converting the input string to lowercase before processing.