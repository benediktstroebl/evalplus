```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    :param string: The input string
    :return: The number of distinct characters
    """
    # Convert the string to lowercase to ignore case
    string = string.lower()
    
    # Initialize an empty set to store unique characters
    unique_chars = set()
    
    # Iterate over each character in the string
    for char in string:
        # Add the character to the set
        unique_chars.add(char)
    
    # Return the number of distinct characters
    return len(unique_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

However, this solution can be optimized further by directly converting the string to a set. A set in Python is an unordered collection of unique elements. This means that every element in a set is unique and the set will automatically remove any duplicates. Here's the optimized version:

```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    
    :param string: The input string
    :return: The number of distinct characters
    """
    # Convert the string to lowercase to ignore case and count distinct characters
    return len(set(string.lower()))

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

This optimized solution has a time complexity of O(n), where n is the length of the string, because creating a set takes linear time. This is more efficient than the original solution, which has a time complexity of O(n log n) due to the sorting that occurs when the set is created from a list.