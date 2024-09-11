```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.
    """
    # Convert the string to lower case to ensure case insensitivity
    lower_case_string = string.lower()
    
    # Convert the string to a set, which automatically removes duplicates
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
print(count_distinct_characters('aaaa'))    # Expected output: 1
print(count_distinct_characters('abcde'))   # Expected output: 5
print(count_distinct_characters('AaBbCc'))  # Expected output: 3
```

In this script, we define a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, regardless of case. We use the `lower()` method to convert the string to lower case, and then convert the string to a set to remove duplicates. Finally, we return the length of the set, which represents the number of distinct characters.

We also include some test cases to demonstrate the function's behavior.