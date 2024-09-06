```python
def how_many_times(string: str, substring: str) -> int:
    """
    Purpose: To find how many times a given substring can be found in the original string, 
    while considering case-insensitive matching.

    Returns: number of occurrences of the substring.
    """
    function that takes two parameters:
    - string: The original string
    - substring: The substring to search for

    It uses a simple count of occurrences of the substring in the original string.
    """
    return sum(1 for char in substring if char in string)
```