Here's a Python script with a self-contained function that solves the problem:
```python
def how_many_times(string, substring):
    return string.count(substring)
```
The function `how_many_times` takes two parameters, `string` and `substring`, and returns the number of times the substring appears in the string, including overlapping instances. This is achieved via the use of the `count` method in Python, which returns the number of occurrences of substring substr in string.