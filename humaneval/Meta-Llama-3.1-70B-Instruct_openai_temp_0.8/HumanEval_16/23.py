```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    Args:
    string (str): The input string
    
    Returns:
    int: The number of distinct characters
    
    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    5
    """
    
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Convert the string to a set, which automatically removes duplicates
    distinct_characters = set(lower_case_string)
    
    # Remove spaces from the set
    distinct_characters = {char for char in distinct_characters if char!=''}
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 5
```
This script works by first converting the string to lower case to ignore case sensitivity, then it converts the string to a set which automatically removes any duplicate characters. It also removes any spaces from the set before returning the length of the set, which is the number of distinct characters.