Here's a self-contained Python function that finds the number of times a given substring can be found in the original string:

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    :param string: The input string
    :param substring: The substring to search
    :return: Number of occurrences of the substring
    """
    return sum(1 for _ in string.find(substring, string))
```

This function loops over every character in the string and counts how many of them match the given substring.