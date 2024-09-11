### Distinct Characters Counter
```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case differences
    lower_case_string = string.lower()
    
    # Use a set to store unique characters
    distinct_chars = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```
This script defines a function `count_distinct_characters` that takes a string as input, converts it to lowercase to ignore case differences, and uses a set to count the number of distinct characters. The example usage demonstrates how to use the function with the given test cases.