```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function uses the `count()` method to detect the substring in the original string. This method returns the number of occurrences of the substring in the original string, regardless of case and overlapping instances.