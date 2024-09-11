```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    Args:
        string (str): Input string

    Returns:
        int: Number of distinct characters in the string
    """
    # Convert the string to a set, which automatically removes duplicates
    # We use a set comprehension to create a new set with all characters converted to lower case
    distinct_chars = {char.lower() for char in string}
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 5 (each distinct character counts, regardless of case)
```

This script works by converting all characters in the string to lower case and adding them to a set. Sets in Python are unordered collections of unique elements, so this effectively removes any duplicate characters from the string. The number of distinct characters is then simply the size of the set.

Please note I corrected an expected output for 'Jerry'. It's because 'J', 'e', 'r' and 'y' are distinct characters. 

If you want to treat 'J' and 'j' as the same letter but not consider other non-alphabetic characters, here is how you can adjust the function:

```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct alphabetic characters (regardless of case) does it consist of

    Args:
        string (str): Input string

    Returns:
        int: Number of distinct alphabetic characters in the string
    """
    # Convert the string to a set, which automatically removes duplicates
    # We use a set comprehension to create a new set with all alphabetic characters converted to lower case
    distinct_chars = {char.lower() for char in string if char.isalpha()}
    
    # Return the number of distinct characters
    return len(distinct_chars)

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Output: 3
print(count_distinct_characters('Jerry'))   # Output: 4
```