```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function that counts the occurrences of a substring in a string.
    :param string: The input string
    :param substring: The substring to find
    :return: Number of occurrences of the substring in the input string
    """
    return _how_many_times(string, substring)

def _how_many_times(string, substring):
    count = 0
    start = 0
    length_string = len(string)
    length_substring = len(substring)

    while start < length_string:
        if string[start:start+length_substring] == substring:
            count += 1
        start += 1

    return count
```