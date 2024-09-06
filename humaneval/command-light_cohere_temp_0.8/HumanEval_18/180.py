```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.count(substring))

# Test cases
test_string = "aaaaaaa"
test_substring = "a"
test_result = how_many_times(test_string, test_substring)
print(test_result)  # Output: 3

# Correctness test
another_string = "hello"
another_substring = "lo"
another_result = how_many_times(another_string, another_substring)
print(another_result)  # Output: 2
```