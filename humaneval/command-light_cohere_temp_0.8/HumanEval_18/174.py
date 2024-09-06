```python
def how_many_times(string: str, substring: str) -> int:
    """
    This function returns the number of occurrences of a given substring in the original string, 
    taking care of overlapping matches.
    """
    Example string and substring, split them into a list of characters
    """
    string = string.split()
    string = [char for char in string]
    substring = substring.split() substring = [char for char in substring]

    # Count occurrences from both ends
    count = 0
    for i, j in zip(string, substring):
        if j == i:
            count += 1

    return count
```