### Count Distinct Characters in a String
#### Problem Statement
Given a string, find out how many distinct characters (regardless of case) it consists of.

#### Solution
```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
    string (str): The input string

    Returns:
    int: The number of distinct characters in the string

    Example:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lowercase_string = string.lower()
    
    # Use a set to store unique characters
    distinct_characters = set(lowercase_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)

# Example usage
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```
This script defines a function `count_distinct_characters` that takes a string as input, converts it to lowercase to ignore case sensitivity, and uses a set to store unique characters. The number of distinct characters is then returned as the length of the set.