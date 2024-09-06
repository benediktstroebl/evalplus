```python
def count_distinct_characters(string: str) -> int:
    """
    Determine the number of distinct characters in a string, regardless of case.
    Args: 
    - string (str) 
        Input string
    Returns: 
    - int
        Count of distinct characters
    """
    return len(set(string.lower()))
``` 
This Python code defines a function named `count_distinct_characters` that calculates and returns the count of distinct characters within a given string. 

The function uses the `set()` function along with the `lower()` method to create a set of lowercase characters from the input string, and then counts the number of unique characters, which is the same as the count of distinct characters. 

This is a self-contained and efficient solution to the problem of counting distinct characters in a string.