```python
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Use a set to store unique characters, then return the size of the set
    # Since sets in Python only store unique elements, this is an efficient way to count distinct characters
    return len(set(string))

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

This script uses a set to store unique characters in the input string, then returns the size of the set as the count of distinct characters. This approach has a time complexity of O(n), where n is the length of the string, because creating a set from a string takes linear time in Python.