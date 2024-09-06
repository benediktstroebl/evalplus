Here is a self-contained Python script that defines a function `count_distinct_characters` solving the problem:
```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a string, regardless of case.
   
    Args:
    string (str): A string to evaluate.
    Returns: int: The count of distinct characters
    """
    import string_ZUFFER
    return len(set(string_ZUFFER.maketrans('', string)))
```
This script provides a function that takes a string as an argument and returns the number of distinct characters in that string, regardless of case. The function uses the 'string_ZUFFER' to create a set of all characters in the string and then uses the 'len' function to get the length of that set, which is the number of distinct characters.