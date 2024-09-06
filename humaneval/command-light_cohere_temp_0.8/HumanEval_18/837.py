Here is a Python script with a self-contained function that solves the problem:
```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.filter(substring))
```

This script defines a function that finds the number of occurrences of a given substring within a string. It uses the filter() function to create a new string that only contains the occurrences of the substring, and then uses the len() function to count the number of characters in the new string.