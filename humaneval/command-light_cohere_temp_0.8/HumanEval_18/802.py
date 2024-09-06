```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test cases
test_str = "aaaaaa"
test_substring = "a"
test_result = how_many_times(test_str, test_substring)
print(test_result) # Output: 3

test_str = "hello"
test_substring = "o"
test_result = how_many_times(test_str, test_substring)
print(test_result) # Output: 2

test_str = "foo"
test_substring = "o rad"
test_result = how_many_times(test_str, test_substring)
print(test_result) # Output: 1
```