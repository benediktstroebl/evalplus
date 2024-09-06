```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```
This function utilizes the `find()` method of Python's string objects to locate the given substring in the string. It then returns the new integer based on the total number of times the substring appears in the original string. 

Please note that this function does not handle overlapping substring cases and it's meant to be self-contained and quick.