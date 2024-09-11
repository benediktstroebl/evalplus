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
    5
    """

    # Convert the string to a set, which automatically removes duplicates
    # Use a set comprehension to convert each character to lower case before adding to the set
    distinct_characters = {char.lower() for char in string}

    # Return the number of distinct characters, which is the size of the set
    return len(distinct_characters)


# Test the function
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
```
This script defines a function `count_distinct_characters` that takes a string as input, converts it to a set of distinct characters (regardless of case), and returns the size of the set. The function is then tested with two examples.