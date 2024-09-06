```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

This function uses the `find()` method from the string module to count the number of occurrences of the `substring` in the `string`. The function then returns the count. 

This is a self-contained function, meaning it can be used without relying on any other functions. It is designed to be a stand-alone solution to the problem. 

Note that the `find()` method might not return the first occurrence, it returns the first occurrence if it's available.