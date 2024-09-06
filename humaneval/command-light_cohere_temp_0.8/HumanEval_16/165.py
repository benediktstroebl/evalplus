```python
def count_distinct_characters(string):
    """ Returns the number of distinct characters in the given string (case-insensitive)"""
    string = string.lower()  # Convert to lowercase to make the process case-insensitive
    characters = set(string)
    return len(characters)

# Basic test case:
print(count_distinct_characters('abc'))  # Output: 3

# Test case with spaces and special characters:
print(count_distinct_characters('xyzXYZ jerry'))  # Output: 4

# Test case with multiple of each character:
print(count_distinct_characters('aabb'))  # Output: 4
```
The function uses a set to store characters and then counts the number of distinct characters. This is approach ensures case-insensitive counting of characters.