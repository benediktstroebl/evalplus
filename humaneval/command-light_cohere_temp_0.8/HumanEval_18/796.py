Here's a self-contained Python script that defines a function `how_many_times`, which finds the number of occurrences of a given substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string.

    Parameters:
    string (str): The input string
    substring (str): The substring to search for

    Returns: count (int): The number of occurrences of substring in string
    """
    return sum(1 for x in string.has(substring))
```

This script provides a function that uses the `has()` method of each character in the string to count how many times the substring appears.