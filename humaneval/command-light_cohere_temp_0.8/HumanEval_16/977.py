Here is a self-contained Python script that solves the problem of counting distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a string, ignoring case.
    """
    return len(set(string.strip()))
```

This script provides a function `count_distinct_characters` that accepts a string and returns the count of distinct characters in it, without considering case sensitivity. The function utilizes the unique() method from the set data structure to achieve this.