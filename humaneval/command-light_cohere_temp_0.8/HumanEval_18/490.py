```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```
The above function uses the `find()` method from the string module to count the occurrences of the substring in the original string.