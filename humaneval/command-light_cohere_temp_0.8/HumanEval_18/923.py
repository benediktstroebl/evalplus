```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of times the given substring can be found in the original string, 
    ignoring case and taking overlapping substrings into account.
    """
    string: The input string
    substring: The input substring to search for
    """
    return sum(1 for x if string.find(substring, x, 0, x==len(substring)))

# Test the function with some examples
string = "aaaaaa"
substring = "aa"
print(how_many_times(string, substring))  # Output: 3
```