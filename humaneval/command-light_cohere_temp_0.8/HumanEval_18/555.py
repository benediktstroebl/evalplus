```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the occurrences of a substring in the original string.
    :param string: str - The input string
    :param substring: str - The substring to search
    :return: int - The number of occurrences of the substring in the string
    """
    return sum(1 for _ in string.contains(substring))
```

The code has a function `how_many_times` that counts the occurrences of a given substring in a string. The function uses the efficient `sum` function that iterates over all the elements in the string and counts the number of occurrences of the substring.