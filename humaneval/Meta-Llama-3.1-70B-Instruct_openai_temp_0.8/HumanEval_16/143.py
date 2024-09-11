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
    # Convert the string to lower case to ignore case sensitivity
    distinct_chars = set(string.lower())
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Example use cases:
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

This script defines a function `count_distinct_characters` that takes a string as input, converts it to lower case, and then uses a set to remove any duplicate characters. The function then returns the number of distinct characters, which is the size of the set. The script also includes example use cases to demonstrate how the function works.