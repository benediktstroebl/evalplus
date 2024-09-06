Here's a self-contained Python function that solves the problem you described: 

```python
def how_many_times(string, substring):
    return len(string.find(substring, string))
```

This function uses the `find()` method from the string module to find all occurrences of the substring in the original string.