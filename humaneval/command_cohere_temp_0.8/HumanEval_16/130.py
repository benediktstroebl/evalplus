Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The `count_distinct_characters` function takes a string as input and returns the number of distinct characters within the string, regardless of case. It converts each character in the input string to lowercase using the `lower()` method, which makes the characters case-insensitive and therefore, considered as the same character. These characters are then collected in a `set` data structure which inherently does not allow duplicate values, so each character is considered only once. The function then returns the size of this set, which is the number of distinct characters in the string.

Here's the documentation for the function which reflects the provided example problems:
```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters (regardless of case) in a string.

    Parameters:
        string (str): The input string.

    Returns:
        int: The number of distinct characters in the string.

    Example:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
```