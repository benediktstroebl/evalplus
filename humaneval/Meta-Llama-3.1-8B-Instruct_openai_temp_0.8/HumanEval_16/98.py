```markdown
## Count Distinct Characters in a String
### Problem Description

Given a string, find out how many distinct characters (regardless of case) does it consist of.

### Solution

```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): The input string

    Returns:
        int: The number of distinct characters in the string

    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lower case to make the comparison case-insensitive
    string = string.lower()
    
    # Use a set to store unique characters and return the size of the set
    return len(set(string))

# Test the function
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))  # Output: 4
```

### Explanation

The `count_distinct_characters` function works by first converting the input string to lower case using the `lower()` method. This is done to make the comparison case-insensitive.

Then, it uses a set to store unique characters from the string. Since sets in Python cannot contain duplicate elements, the size of the set will be equal to the number of distinct characters in the string.

Finally, the function returns the size of the set using the `len()` function.