```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```
The function '**`how_many_times`**' takes two parameters: a string and a substring. It uses the string.find() function to find the how substring in the string and returns the number of matches.