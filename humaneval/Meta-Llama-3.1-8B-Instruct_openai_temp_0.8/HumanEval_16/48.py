```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string
    """
    # Convert the string to lower case to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters
    unique_characters = set(lower_case_string)
    
    # Return the number of unique characters
    return len(unique_characters)

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

In this script, we first convert the input string to lower case to ignore case sensitivity. Then, we use a set to store unique characters from the string. Since sets in Python cannot contain duplicate elements, the set will automatically remove any duplicate characters. Finally, we return the number of unique characters by getting the length of the set.