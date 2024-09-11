### Counting Distinct Characters in a String
```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
    string (str): The input string to count distinct characters from

    Returns:
    int: The number of distinct characters in the string

    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case
    lower_string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set(lower_string)
    
    # Return the count of unique characters
    return len(unique_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```
This script defines a function `count_distinct_characters` that takes a string as input, converts it to lowercase to ignore case, and uses a set to store unique characters. The function returns the count of unique characters, which is the length of the set. The script also includes test cases to demonstrate the function's usage and expected output.