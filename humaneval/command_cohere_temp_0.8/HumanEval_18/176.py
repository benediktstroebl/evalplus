```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function counts the number of times the substring occurs in the string, including cases of overlapping. It does so by using the built-in `count` method of Python strings to find the occurrence of the substring in the parent string. This method returns an integer representing the number of times the substring appears in the string, even if they overlap. 

Such a simple solution is suitable for this problem because the problem statement explicitly states that the function `how_many_times` should return an integer that counts the number of times the substring occurs, even if they overlap.