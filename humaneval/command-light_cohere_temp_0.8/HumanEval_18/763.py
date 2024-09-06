```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```
The function uses the `find()` method to search the substring in the given string. It returns the finding the recent and distinct matches.