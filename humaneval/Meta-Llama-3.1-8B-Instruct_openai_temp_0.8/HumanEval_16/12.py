```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) it consists of.

    Args:
    string (str): The input string

    Returns:
    int: The number of distinct characters in the string
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters and find the size of the set
    # A set automatically removes duplicates
    distinct_chars = set(lower_case_string)
    
    return len(distinct_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

In this script, we first convert the input string to lower case to ensure that we are counting the same characters regardless of case. Then, we use a set to store unique characters. Since a set automatically removes duplicates, the size of the set gives us the number of distinct characters in the string.