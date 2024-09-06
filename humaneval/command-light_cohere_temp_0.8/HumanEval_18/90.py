Here is a self-contained Python script with a function that solves the problem you have described:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring using its length.

    Parameters: 
    string (str): The input string 
    substring (str): The substring to search for 
    Returns: number of occurrences of substring in string, or 0 if substring is not found
    """

    if len(substring) > len(string):
        return 0

    count = 0
    i = len(string) - 1
    while i >= 0:
        if string[i:i+len(substring)] == substring:
            count += 1
        i -= 1

    return count
```