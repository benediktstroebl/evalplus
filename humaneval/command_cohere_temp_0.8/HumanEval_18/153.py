Here's a Python script that contains a function called `how_many_times` which takes a string and a substring as input and returns the number of times the substring occurs within the string, including overlapping occurrences:
```python
def how_many_times(string: str, substring: str) -> int:
    return string.count(substring)
```
The function leverages the `count` method of strings in Python to identify and tally the occurrences of the substring within the string, including instances where the substring overlaps with itself.