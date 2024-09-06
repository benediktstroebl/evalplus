Here's a self-contained Python function that solves the problem you described:
```python
def how_many_times(string, substring): 
    return len(string.find(substring))
```

This function uses the `find()` method from the string module to count the number of occurrences of the substring in the original string.