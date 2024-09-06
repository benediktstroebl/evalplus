Here is a self-contained Python script that defines a function to solve the problem you described:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string.
    If required to handle overlapping matches.
    """
    string: The input string 
    substring: The substring to find in the string
    Returns: number of occurrences of the substring in the string
    """
    return len(string.find(substring))
```

This script has a function that uses the `find()` method from the `string` module to count the number of occurrences of a given `substring` in a given `string`.