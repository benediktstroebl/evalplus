```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
    string (str): The input string

    Returns:
    int: The number of distinct characters in the string

    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Use a set to keep track of unique characters
    unique_chars = set(string)
    
    # Return the number of unique characters
    return len(unique_chars)

# Test the function
if __name__ == "__main__":
    print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
    print(count_distinct_characters('Jerry'))  # Expected output: 4
    print(count_distinct_characters('HelloWorld'))  # Expected output: 8
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, ignoring case. It uses a set to keep track of unique characters, as sets in Python automatically eliminate duplicates. The `if __name__ == "__main__":` block is used to test the function with some example inputs.