```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.
    """
    # Convert the string to lower case to handle case insensitivity
    lower_case_string = string.lower()
    
    # Convert the string to a set, which removes duplicate characters
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```
This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, regardless of case. The function first converts the string to lower case, then converts it to a set (which removes duplicate characters), and finally returns the size of the set. The test cases at the end of the script demonstrate the function's usage and expected output.