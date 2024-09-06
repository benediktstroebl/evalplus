```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

This function finds the number of times a given substring can be found in the original string, using the `find()` function. It returns the
number of occurrences and can handle overlapping cases. 

This is a self-contained function that can be used to solve the problem.