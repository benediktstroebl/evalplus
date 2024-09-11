```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case
    lower_case_string = string.lower()
    
    # Convert the string to a set to get distinct characters
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```
This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, regardless of case. It uses Python's built-in `set` data structure to efficiently find the distinct characters. The script also includes test cases to demonstrate its usage and verify its correctness.