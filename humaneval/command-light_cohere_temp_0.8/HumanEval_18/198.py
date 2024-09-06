```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```
This function uses the find() method of the string object to count the occurrences of a given substring in the original string.