```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    # Use a set to store unique characters
    unique_chars = set(string)
    # The number of distinct characters is the size of the set
    return len(unique_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))  # Expected output: 4
```

In this script, we define a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters it contains. We use a set to store unique characters because sets in Python only store unique elements. The size of the set is then the number of distinct characters. We convert the string to lowercase using the `lower` method to ignore case sensitivity.