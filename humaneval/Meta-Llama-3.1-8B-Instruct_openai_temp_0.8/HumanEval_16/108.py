```python
def count_distinct_characters(string: str) -> int:
    """ 
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
    string (str): The input string

    Returns:
    int: The number of distinct characters in the string

    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Convert the string into a set, which automatically removes duplicates
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

In this script, we first convert the input string to lowercase using the `lower()` method. This ensures that we don't count the same character in both uppercase and lowercase forms.

Then, we convert the string into a `set`, which automatically removes any duplicate characters. The `len()` function is then used to count the number of elements in the set, which gives us the number of distinct characters in the original string.

The test cases at the end of the script demonstrate how to use the `count_distinct_characters()` function.