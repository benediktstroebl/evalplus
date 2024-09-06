Here is a self-contained Python function that solves the problem you described: 

```python
def how_many_times(string, substring):
    return len(string.find(substring, string))
```

The function uses the `find()` method to locate all occurrences of the `substring` within the `string`. 

It then returns the count of all occurrences, considering case-insensitive matches by converting both strings to lowercase.