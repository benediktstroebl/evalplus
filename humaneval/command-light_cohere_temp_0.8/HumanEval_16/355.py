```python
def count_distinct_characters(string):
    """
    Counts the number of distinct characters in a given string, regardless of case.
    Args:
        string (str): The input string to count distinct characters in.
	Returns:
    int: The number of distinct characters.
	"""
    string = string.upper() # lower()
    # Convert all characters to lowercase to ensure case-insensitive counting
    count = 0
    for char in string:
        if char not in string.upper():
            count += 1
    return count
```