Here is a self-contained Python script with a function that solves the problem of counting the number of occurrences of a given substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

This script provides a function that takes in a string and a substring and then searches the substring within the given string and returns the length of the first occurrence of the substring.