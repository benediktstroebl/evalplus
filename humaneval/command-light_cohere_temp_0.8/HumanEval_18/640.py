Here's the solution to the problem that you asked:
```python
def how_many_times(string, substring):
    return len([x for x in string.search(substring])
```
This function uses the `search()` method for each substring in the input string to count the number of occurrences.