### Count Distinct Characters in a String

This Python script defines a function `count_distinct_characters` that takes a string as input and returns the count of distinct characters, ignoring case.
```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The count of distinct characters

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case
    string = string.lower()
    
    # Use a set to store unique characters
    distinct_chars = set(string)
    
    # Return the count of distinct characters
    return len(distinct_chars)


# Example usage
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```
This script defines the function `count_distinct_characters` with a docstring that explains its purpose, arguments, return value, and provides examples of usage. The function converts the input string to lowercase, uses a set to store unique characters, and returns the count of distinct characters. The script also includes example usage to demonstrate the function's behavior.