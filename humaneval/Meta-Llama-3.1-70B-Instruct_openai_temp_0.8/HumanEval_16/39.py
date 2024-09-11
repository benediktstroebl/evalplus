```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of.

    Args:
    string (str): Input string.

    Returns:
    int: Number of distinct characters in the string.
    """
    return len(set(char.lower() for char in string if char.isalpha()))

# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 4
```
This script works by using a set to store unique characters (converted to lowercase to ignore case differences) from the input string. The `isalpha()` method ensures that only alphabets are considered. The `len()` function then returns the number of distinct characters in the string.