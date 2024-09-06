```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in string if char == substring)
    
# Test cases
test_str = "aaaaaa"
test_sub = "a"
test_result = how_many_times(test_str, test_sub)
assert test_result == 3, "Test failed: '" + str(test_result) + "'"

test_str = "abcde"
test_sub = "a"
test_result = how_many_times(test_str, test_sub)
assert test_result == 4, "Test failed: '" + str(test_result) + "'"

test_str = "hello world!"
test_sub = "o"
test_result = how_many_times(test_str, test_sub)
assert test_result == 5, "Test failed: '" + str(test_result) + "'"

print("All tests passed!")
```