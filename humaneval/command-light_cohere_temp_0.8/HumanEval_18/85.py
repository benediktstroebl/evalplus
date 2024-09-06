```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

This Python function uses the `find()` method to locate the given substring in the string. The function then returns the number of times the substring appears in the string, not counting cases where the substring is repeated. 
Here is a self-contained test function that uses the function to check if a specific input produces the correct result: