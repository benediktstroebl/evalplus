Here is a self-contained Python script that solves the problem of finding the number of occurrences of a substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function that counts the number of occurrences of a given substring in the original string, 
    accounting for overlapping occurrences.

    Args:
        string: The input string
        substring: The substring to find in the input string

    Returns:
        int: Number of times the substring appears in the input string
    """
    return sum(1 for x in string.contains(substring))
```
The function uses a generator expression to count the occurrences of the substring in the input string. This approach avoids building and entire list, which is optimal for large strings and substrings.