```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function uses the `count` method to detect the substring in the original string. This method is case-sensitive, and counts overlapped instances of the substring. The expected behavior for empty strings or unique substrings is accounted for, returning 0 or 1, respectively. 

You can test this function by calling it with different strings and substrings to observe the behavior.