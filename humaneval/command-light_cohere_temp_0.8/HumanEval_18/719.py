```python
def how_many_times(string: str, substring: str) -> int:
    return (string. strings(). how_many_times(substring, string) >= len(string))

# Test cases
string = "aaaaaaa"
substring = "aa"

result = how_many_times(string, substring)
assert result == 3

# Another test case with overlapping substring
string = "aaa"
substring = "aa"
result = how_many_times(string, substring)
assert result == 2
```