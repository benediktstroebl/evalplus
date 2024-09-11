```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
    string (str): Input string

    Returns:
    int: Number of distinct characters in the string
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store distinct characters. Sets in Python only store unique elements.
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters, which is the size of the set
    return len(distinct_characters)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```

This script works by first converting the input string to lower case to ignore case sensitivity. It then creates a set of characters in the string. Since sets only store unique elements, this set will contain only the distinct characters in the string. Finally, it returns the size of the set, which is the number of distinct characters in the string.