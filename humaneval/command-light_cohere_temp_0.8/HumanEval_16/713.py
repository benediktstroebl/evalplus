```python
def count_distinct_characters(string):
    """
    Returns the number of distinct characters in the given string, regardless of case.
    Args: 
    string (str): The input string to check for distinct characters.
    Returns: integer (int): The number of distinct characters in the string.
    """
    string = str.strip() 
    # return a number = set(string).string()
    return len(number)

# Test the function
assert(count_distinct_characters('xyzXYZ') == 3)
assert(count_distinct_characters('Jerry') == 4)
```