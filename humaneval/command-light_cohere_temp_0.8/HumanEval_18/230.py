```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for i, char in enumerate(string) if char == substring)
    
# tests
test_str = "aaaaaa"
test_substring = "a"
assert how_many_times(test_str, test_substring) == 3

test_str = "abc"
test_substring = "ab"
assert how_many_times(test_str, test_substring) == 2

test_str = "hello"
test_substring = "o"
assert how_many_times(test_str, test_substring) == 0
```