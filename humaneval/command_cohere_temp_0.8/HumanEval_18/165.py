```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function counts the number of times the substring occurs in the string, including overlapping instances. It does so by using the built-in `count` method of Python strings, which returns the number of times the substring appears in the string. The method also counts overlapping instances, which are cases where the substring appears multiple times in the same position.