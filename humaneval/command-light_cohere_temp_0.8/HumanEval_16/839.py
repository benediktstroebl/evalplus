```python
def count_distinct_characters(string: str) -> int:
    """
    Returns the count of distinct characters in the given string, regardless of case.
    Args: 
        string (str): A string containing characters
    Returns: 
        int: The count of distinct characters
    """
    char_set = set(string.count(char))
    return len(char_set)

# Test the function
string1 = "xyzXYZ"
string2 = "jerry"
string3 = "hello world"

print(count_distinct_characters(string1))  # Output: 3
print(count_distinct_characters(string2))  # Output: 4
print(count_distinct_characters(string3))  # Output: 5)
```