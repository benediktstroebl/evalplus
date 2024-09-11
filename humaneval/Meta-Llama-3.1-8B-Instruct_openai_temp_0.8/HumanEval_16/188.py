### Counting Distinct Characters in a String
```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Example usage:
if __name__ == "__main__":
    print(count_distinct_characters('xyzXYZ'))  # Output: 3
    print(count_distinct_characters('Jerry'))  # Output: 4
```
This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters it consists of, ignoring case sensitivity. The function works by converting the string to lowercase and then using a set to store unique characters. The number of elements in the set is the number of distinct characters.