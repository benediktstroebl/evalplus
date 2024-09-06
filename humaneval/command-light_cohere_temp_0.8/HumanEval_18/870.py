Here is a self-contained Python script with a function that solves the problem of finding how many times a given substring can be found in the original string, while accounting for overlapping occurrences:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    subIndex = string.find(substring, 0)
    
    while subIndex != -1:
        count += 1
        subIndex = string.find(substring, subIndex + len(substring))
    
    return count
```