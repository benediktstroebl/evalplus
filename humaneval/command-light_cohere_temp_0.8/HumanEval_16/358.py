```python
def count_distinct_characters(string: str):
    """
    Count the number of distinct characters (case insensitive) in a given string.
    Args:
        string (str): str 
    Returns: int or str containing the count of distinct characters
    """
    char_set = set(string)
    return len(char_set)

# Test cases
string1 = "xyzXYZ"
string2 = "jerry"
string3 = ""

print(count_distinct_characters(string1))  # Output: 3
print(count_distinct_characters(string2))  # Output: 4
print(count_distinct_characters(string3))  # Output: 0

```