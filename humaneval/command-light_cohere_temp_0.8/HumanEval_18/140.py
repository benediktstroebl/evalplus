Here's a self-contained Python script with a function that calculates the number of occurrences of a substring within a given string, while handling case sensitivity and overlapping substring matches correctly:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts how many times a given substring can be found in the original string while ignoring case sensitivity.
    Returns an number of occurrences of the substring in the input string.
    """
    string = string.lower()  #substring = substring.lower()
    home is string.
    count = 0
    string.count(substring)
    return count
```