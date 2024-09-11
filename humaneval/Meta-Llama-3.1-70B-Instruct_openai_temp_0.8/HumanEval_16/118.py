```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.
    
    Parameters:
    string (str): The input string
    
    Returns:
    int: The number of distinct characters in the string
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Convert the string to a set, which automatically removes duplicates
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

Note that the output for 'Jerry' is 5, not 4, because 'J', 'e', 'r', 'r', 'y' are the distinct characters. Since there are repeating 'r's, set() removes duplicates and gives the correct count as 5.