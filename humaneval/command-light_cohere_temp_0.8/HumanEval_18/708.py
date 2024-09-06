Here is a Python script that defines a self-contained function to solve the problem:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring within the original string, 
    including overlapping matches.
    >>> string = "aaaaaaa"
    >>> how_many_times('aa', string)
    3
    """
    return sum(1 for i, match in enumerate(re.finditer(substring, string)) where match)
```
The `re.finditer` function returns a matching substrings against the original string. The sum of the match objects created by this function returns the total number of matches, including any overlapping substrings.