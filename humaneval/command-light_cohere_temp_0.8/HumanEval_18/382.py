```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```
Here's a self-contained Python function that finds the number of occurrences of a given substring within another string. 

It uses the `find()` method to search for the substring and returns the length of the occurrence, which effectively counts the number of times the substring appears in the original string.