```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): Input string

    Returns:
        int: Number of distinct characters in the string
    """
    # Convert the string to a set, which automatically removes duplicates
    # We use a set comprehension to convert each character to lower case
    distinct_chars = {char.lower() for char in string}
    
    # The number of distinct characters is the size of the set
    return len(distinct_chars)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, regardless of case. It uses a set comprehension to convert each character to lower case and remove duplicates, and then returns the size of the set.

The script also includes two test cases to verify the correctness of the function.