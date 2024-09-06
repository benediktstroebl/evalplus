```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```
This function uses the `find()` method to search for the substring. 
It returns the number of times the substring appears in the string.