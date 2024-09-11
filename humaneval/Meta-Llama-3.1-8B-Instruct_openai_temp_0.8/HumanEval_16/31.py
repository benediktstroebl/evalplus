```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Convert the string to a set, which automatically removes duplicates
    distinct_chars = set(string)
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test the function
if __name__ == "__main__":
    print(count_distinct_characters('xyzXYZ'))  # Should print 3
    print(count_distinct_characters('Jerry'))  # Should print 4
```

This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters it contains. The function works by converting the string to lowercase to ignore case sensitivity, then converting the string to a set which automatically removes duplicates. The number of distinct characters is then returned as the length of the set.