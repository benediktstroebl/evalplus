```markdown
### Distinct Characters Counter

This Python script counts the number of distinct characters in a given string, ignoring case sensitivity.

#### Code

```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
    string (str): The input string to count distinct characters from

    Returns:
    int: The number of distinct characters in the string

    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    lower_case_string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set(lower_case_string)
    
    # Return the number of unique characters
    return len(unique_chars)

# Example usage:
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```

#### Explanation

The `count_distinct_characters` function works as follows:

1. Convert the input string to lowercase using the `lower()` method to ignore case sensitivity.
2. Create a set from the lowercase string using the `set()` function. Sets in Python automatically remove duplicate elements.
3. Return the number of unique characters by getting the length of the set using the `len()` function.

This approach has a time complexity of O(n), where n is the length of the input string, because creating a set requires iterating over all characters in the string. The space complexity is also O(n) because in the worst case, all characters in the string are unique and stored in the set.