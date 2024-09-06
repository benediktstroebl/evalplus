Here is a self-contained Python script that solves the problem of counting the number of occurrences of a substring within a string:
```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

This script defines a function `how_many_times` that takes two arguments: a string and a substring. The function then uses the string's `find()` method to count the number of occurrences of the substring.

The function then returns the count of occurrences.