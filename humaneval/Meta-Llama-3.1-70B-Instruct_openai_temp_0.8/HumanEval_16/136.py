```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Args:
    string (str): Input string
    
    Returns:
    int: Number of distinct characters in the string
    """
    # Convert the string to a set to remove duplicate characters
    # The set data structure in Python is an unordered collection of unique elements
    # We use the casefold() method to convert the string to lowercase and then to a set
    # This is because sets in Python are case sensitive
    distinct_chars = set(string.casefold())
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```
This script defines the `count_distinct_characters` function as specified, then tests it with the given examples. It first converts the input string to a set, which automatically removes any duplicate characters. The `casefold()` method is used to convert the string to a case-insensitive format before creating the set, so that the same characters in different cases are not treated as distinct. Finally, the function returns the number of distinct characters, which is just the size of the set.