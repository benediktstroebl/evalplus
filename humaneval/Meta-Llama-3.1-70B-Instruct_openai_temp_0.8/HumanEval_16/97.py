```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Convert the string to a set, which automatically removes duplicates
    distinct_chars = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

You can save this script to a file (e.g., `distinct_chars.py`) and run it using Python (e.g., `python distinct_chars.py`) to see the test results. The `count_distinct_characters` function takes a string as input, converts it to lowercase to ignore case sensitivity, removes duplicates by converting it to a set, and returns the number of distinct characters.