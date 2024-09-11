### Distinct Characters Counter
#### A Python Script to Count Distinct Characters in a String
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
    lower_string = string.lower()
    
    # Use a set to store unique characters, sets in Python are unordered collections of unique elements
    distinct_chars = set(lower_string)
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```
This script works by first converting the input string to lowercase to ignore case sensitivity. It then creates a set of unique characters from the string using the `set()` function. Finally, it returns the number of elements in the set, which represents the number of distinct characters in the string.