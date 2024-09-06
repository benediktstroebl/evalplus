```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

This function employs the `find()` method from the string module to locate the substring within the original string. It then returns the difference between the occurrences of the substring. 

You can use this function to determine the number of occurrences of a given substring in a string.