```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
    string (str): Input string to count distinct characters from

    Returns:
    int: The number of distinct characters in the string
    """
    # Convert the string to lowercase to ignore case differences
    lower_case_string = string.lower()
    # Convert the string into a set, which automatically removes duplicates
    distinct_characters = set(lower_case_string)
    # The number of distinct characters is the size of the set
    return len(distinct_characters)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

In this script, we define a function `count_distinct_characters` that takes a string as input, converts it to lowercase, and then uses a set to keep track of the distinct characters. The `len` function is then used to return the number of distinct characters. We also include two test cases to demonstrate the usage of this function.