```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Convert the string to a set, which automatically removes duplicates
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)


# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

In this script, we define the function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string. We convert the string to lower case to ignore case sensitivity, then convert the string to a set to remove duplicates. Finally, we return the length of the set, which represents the number of distinct characters.

The script also includes example usage of the function, demonstrating how to call the function with different inputs and print the results.