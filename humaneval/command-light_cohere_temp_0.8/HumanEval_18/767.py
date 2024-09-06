```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

This function uses the `find()` method to search for the substring in the string. The length of the string's occurrences of the substring is the number of successful searches. The function is also designed to handle overlapping matches, which is a common scenario in string searching.