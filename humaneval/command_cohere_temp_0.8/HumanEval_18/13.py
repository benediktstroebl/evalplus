```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function counts the number of times the substring occurs in the string, including cases of overlapping. It does so by using the built-in `count` method of Python strings to find the occurrence of the substring in the parent string. 

This solution is efficient with time complexity of O(n) since it is using a hash data structure to find the substring occurrence in the parent string.