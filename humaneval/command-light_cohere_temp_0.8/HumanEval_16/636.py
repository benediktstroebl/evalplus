```python
def count_distinct_characters(string: str):
    """
    Count the number of distinct characters in a given string, regardless of case.
    Args: 
        string (str): The input string to check for distinct characters
    Returns: 
        int: The number of distinct characters
    """
    # Remove all letters using lowercase
    string = ''.join(char for char in string if char.isalpha() == False)
    # Count the distinct characters
    return len([char for char in string if char.isalpha()])
```