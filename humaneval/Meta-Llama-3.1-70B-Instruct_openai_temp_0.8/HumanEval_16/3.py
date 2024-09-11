```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: Number of distinct characters in the string
    """
    # Convert the string to lower case to make the comparison case-insensitive
    lower_case_string = string.lower()
    
    # Convert the string into a set, which automatically removes duplicates
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

In this script, we first convert the string to lower case to make the comparison case-insensitive. Then, we convert the string into a set, which automatically removes duplicates. Finally, we return the number of distinct characters, which is the size of the set.