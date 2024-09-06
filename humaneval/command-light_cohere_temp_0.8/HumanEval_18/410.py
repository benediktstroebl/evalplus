```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in string if char == substring)

# Test cases
test_string = "aaaaaa"
test_substring = "a"
test_result = how_many_times(test_string, test_substring)
assert test_result == 3

# Other cases
test_string = "abc"
test_substring = "b"
test_result = how_many_times(test_string, test_substring)
assert test_result == 1
```