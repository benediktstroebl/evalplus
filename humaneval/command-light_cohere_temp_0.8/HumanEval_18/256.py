Here's the solution:
```python
def how_many_times(string, substring): 
    return len(string.find(substring))
```

This function iterates over every character in the string and counts how many times the substring appears.  It's approach is simple but efficient.