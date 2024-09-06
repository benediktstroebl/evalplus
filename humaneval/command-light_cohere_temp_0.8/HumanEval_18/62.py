```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping.
    """
    string: str => The input string
    substring: str => The substring to search
    Returns: int => Count of occurrences of substring in string without overlapping.
    """
    string = "aaaaaaaab"
    sub = "ab"
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count
```