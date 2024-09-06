Here is a self-contained Python function that solves the problem of finding the number of occurrences of a given substring within a string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds and returns the number of times a given substring can be found in the original string.

    Time complexity: O(n) where n = length of string
    """
    return _how_many_times(string, substring)

def _how_many_times(string, substring):
    count = 0
    i = 0
    while i < len(string):
        if string[i] == substring:
            count += 1
        i += 1
    return count
```

This function iterates through each character in the string and counts the number of occurrences of the substring. You can use this example function to find the number of times a substring appears in a given string.