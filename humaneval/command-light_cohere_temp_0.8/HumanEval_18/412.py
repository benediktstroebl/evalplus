```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count all occurrences of a given substring in the original string.

    Args:
        string (str): str - The original string
        substring (sub): str - The substring to find

    Returns:
        int - Number of occurrences of substring in str
    """
    return len(string.find(substring))
```
The code defines a function how_many_times that takes two arguments: a string and a substring. The function uses the string.find() function to count all occurrences of the substring in the original string. It returns the number of occurrences.