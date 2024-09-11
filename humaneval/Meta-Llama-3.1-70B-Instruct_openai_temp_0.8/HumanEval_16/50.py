```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Args:
        string (str): The input string
    
    Returns:
        int: The number of distinct characters in the string
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Convert the string to a set, which automatically removes duplicates
    distinct_characters = set(lower_case_string)
    
    # The number of distinct characters is the size of the set
    return len(distinct_characters)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

In this script, we define a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, regardless of case. We use the `lower()` method to convert the string to lower case, and the `set` data structure to remove duplicates. The `len()` function then gives us the number of distinct characters.

The script also includes two test cases to demonstrate the function's usage and verify its correctness.