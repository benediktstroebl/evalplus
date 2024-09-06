```python
def count_distinct_characters(string):
    """
    A function to count distinct characters in a given string, regardless of case.
    """
    Counts each character in the string and returns the count.
    """
The string is made using ASCII and consists of all uppercase and lowercase English alphabet (A-Z) and space (32), hence the count is 26.
"""
    # Define the list of ASCII characters
    ASCII_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Initialize a count of distinct characters
    distinct_char_count = sum(1 for char in ASCII_CHARS if char in string.
    # Return the result of the distinct character count
    return distinct_char_count
```