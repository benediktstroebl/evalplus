```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string to count distinct characters from.

    Returns:
        int: Number of distinct characters in the string.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    # Use a set to store unique characters
    unique_characters = set(lower_case_string)
    # Return the number of unique characters
    return len(unique_characters)


# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters (regardless of case) in the string. It uses a set to keep track of unique characters and returns the size of the set, which represents the number of distinct characters. The script also includes example usage to demonstrate the function's behavior.