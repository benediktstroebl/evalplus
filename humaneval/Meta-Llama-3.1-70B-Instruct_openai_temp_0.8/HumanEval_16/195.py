```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.
    """

    # Convert the string to a set to remove duplicates. 
    # We use a set comprehension to convert each character to lower case before adding it to the set.
    distinct_characters = {char.lower() for char in string}

    # Return the number of distinct characters, which is the size of the set.
    return len(distinct_characters)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 5
```

In this script, we define a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string. We use a set comprehension to convert each character to lower case and add it to a set, which automatically removes duplicates. The size of the set is then returned as the result.