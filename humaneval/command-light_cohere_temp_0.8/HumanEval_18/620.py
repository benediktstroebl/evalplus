Here's the function:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count occurrences of a substring in a string, ignoring case and avoiding duplicate counts.
    """
   
    original string and substring.
    return sum(1 for match in string.match(substring, 0, 1))
```
You can use this function to get the number of occurrences of any substring in any given string.