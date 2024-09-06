Here's the solution:

```python
def how_many_times(string, substring): 
    return len(string.find(substring))
```

This function uses the `find()` method to count the occurrences of the substring. 
The `find()` method uses a case-sensitive search to locate the substring within the original string. 
It returns the number of times the substring can be found in the original string, accounting for case and over-laps.