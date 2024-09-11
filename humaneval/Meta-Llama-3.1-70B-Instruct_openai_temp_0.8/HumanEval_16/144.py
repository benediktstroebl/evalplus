```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to get distinct characters
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Test cases
if __name__ == "__main__":
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 5
    assert count_distinct_characters('aaaaaa') == 1
    assert count_distinct_characters('abcdefgh') == 8
    assert count_distinct_characters('') == 0
```