Here's the self-contained Python function that solves the problem you described: 

```python
def how_many_times(string, substring):
    return len([x for x in string.search(substring))
```

This function uses the `search()` method of the `string` and the `substring` argument, which returns the first occurrence of the substring in the string. 

You can use this function by passing the string and the substring as arguments, and it will return the number of occurrences of the substring in the string.