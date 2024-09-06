```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in substring if char in string)

# Test the function
test_string = "aaaaaa"
test_substring = "a"
result = how_many_times(test_string, test_substring)
assert result == 3

# Test again
test_string = "abc"
test_substring = "ab"
result = how_many_times(test_string, test_substring)
assert result == 2
```