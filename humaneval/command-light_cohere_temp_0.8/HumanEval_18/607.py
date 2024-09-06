Here is a self-contained Python script that defines a function to solve the problem of counting the number of occurrences of a given substring within a string:
```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

This script is a straightforward implementation that utilizes the `find()` method of the string object to locate the substring and returns the count of its occurrences. 
The `find()` method returns an iterator, so the length of the match is returned as an integer. 
Please note that this approach does not handle overlapping substring matches and could lead to incorrect results for those cases.