```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.
    """
    # Convert the string to lower case to ignore case differences
    lower_case_string = string.lower()
    
    # Use a set to store unique characters
    unique_characters = set(lower_case_string)
    
    # Return the number of unique characters
    return len(unique_characters)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

In this script, we define a function `count_distinct_characters` that takes a string as input. We convert the string to lower case to ignore case differences, then use a set to store unique characters. Finally, we return the number of unique characters, which is the size of the set.

We also include two test cases to verify the correctness of the function. The expected output for the test cases is printed in the comments.