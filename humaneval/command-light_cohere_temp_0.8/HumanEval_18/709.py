```python
def how_many_times(string: str, substring: str) -> int:
    return (len(string) - len(string.find(substring)))
```

This function counts the occurrences of a substring within a given string, and returns the difference between their lengths. It employs the string.s `find()` method to locate the substring in the original string, and then counts the characters in the original string minus the characters found.