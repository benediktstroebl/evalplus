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
        5
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Convert the string into a set, which automatically removes duplicates
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Test cases
if __name__ == "__main__":
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 5
```
This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, ignoring case sensitivity. It uses a set to automatically remove duplicates and then returns the size of the set. The script also includes test cases to verify the function's correctness.