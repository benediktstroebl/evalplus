```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string
    """
    # Convert the string to a set, which automatically removes duplicates
    # We use a set comprehension to convert each character to lowercase
    # This ensures the function is case-insensitive
    distinct_chars = {char.lower() for char in string}
    
    # The number of distinct characters is the size of the set
    return len(distinct_chars)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```