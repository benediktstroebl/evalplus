**Counting Distinct Characters in a String**
=============================================

Below is a simple Python function that takes a string as input and returns the count of distinct characters in the string, regardless of their case.

```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Args:
    string (str): The input string
    
    Returns:
    int: The count of distinct characters in the string

    Example:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters
    unique_characters = set(lower_case_string)
    
    # Return the count of unique characters
    return len(unique_characters)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

This script works by first converting the input string to lowercase to ignore case sensitivity. It then uses a set to store unique characters from the string. A set in Python is an unordered collection of unique elements, making it ideal for storing unique characters. Finally, it returns the count of unique characters, which is the length of the set.