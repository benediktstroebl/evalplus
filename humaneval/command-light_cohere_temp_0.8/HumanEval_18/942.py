Here is a Python script with a self-contained function that solves the problem:
```python
def how_many_times(string, substring): 
    return len(string.find(substring))
```

This script defines a function, `how_many_times`, which takes two parameters: a string and a substring. The function uses thefind to search the substring in the string, and returns the length of the resulting match.