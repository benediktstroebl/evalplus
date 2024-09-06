```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for i, char in enumerate(string) if char == substring)

# Test cases
test_string = "aaa"
test_substring = "a"
test_result = how_many_times(test_string, test_substring)
assert test_result == 3

test_string = "hello"
test_substring = "o"
test_result = how_many_times(test_string, test_substring)
assert test_result == 2

test_string = "hello world"
test_substring = "o"
test_result = how_many_times(test_string, test_substring)
assert test_result == 2
```