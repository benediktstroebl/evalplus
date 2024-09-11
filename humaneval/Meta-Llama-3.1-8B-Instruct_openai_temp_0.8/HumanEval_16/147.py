```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string to count distinct characters in

    Returns:
        int: The number of distinct characters in the string
    """
    # Convert the string to lower case to ignore case sensitivity
    string = string.lower()
    
    # Use a set to store unique characters and then get the length of the set
    # A set in Python is an unordered collection of unique elements
    distinct_chars = set(string)
    
    return len(distinct_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```

In this script, the `count_distinct_characters` function first converts the input string to lower case to ignore case sensitivity. It then uses a set to store unique characters and returns the length of the set, which represents the number of distinct characters in the string. The test cases at the end verify the correctness of the function.