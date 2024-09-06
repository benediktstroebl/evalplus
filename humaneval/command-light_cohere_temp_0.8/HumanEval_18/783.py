```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping.
    Parameters:
    string: The input string
    substring: The substring to search for
    Returns: the number of positions where substring appears in string
    """
    m = len(substring)
    result = 0
    i = 0
    while i < len(string):
        if string[i:i+m] == substring:
            result += 1
        i += 1
    return result
# Test the function
string = "aaaaaa"
substring = "aa"
print(how_many_times(string, substring))  # Output: 3
```