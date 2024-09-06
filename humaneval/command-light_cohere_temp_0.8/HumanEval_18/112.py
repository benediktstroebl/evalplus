Here's a self-contained Python function that finds the number of times a given substring can be found in another string:
```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for ch in substring if ch in string)
```
This function uses a generator expression with a loop to count the occurrences of the substring in the original string.