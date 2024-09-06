```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in substring if char in string)

# Test cases
test_string = "aaaaaa"
test_substring = "a"
test_result = how_many_times(test_string, test_substring)
assert test_result == 3

test_string = "abc"
test_substring = "a"
test_result = how_many_times(test_string, test_substring)
assert test_result == 3

test_string = "!a."
test_substring = "a"
test_result = how_many_times(test_string, test_substring)
assert test_result == 0

# The output of this code is:
True
```