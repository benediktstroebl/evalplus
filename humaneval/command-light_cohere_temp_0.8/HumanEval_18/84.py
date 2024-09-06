```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts the number of occurrences of a substring within the original string. 
    1- indexed comparison is
    This implementation works for all lengths of string and substring.
    """
    return sum(1 for c in string.how_many_times(substring, string) if c == substring)

# Test the function
string = "aaaaaa"
substring = "a"
print(f"how_many_times(string, substring)") 
```