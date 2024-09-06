```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function accepts a string and a substring and uses the `count()` method to return the number of times the substring occurs in the string. This method counts overlapping instances, so it overlaps, like the `aa` in `aaaa`b.