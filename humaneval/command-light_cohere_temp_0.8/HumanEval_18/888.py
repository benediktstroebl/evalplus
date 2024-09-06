```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, without overlapping.
    >>> string = "aaaaaaa"
    sub = "a"
    result = 0
    for char in string:
        if char == sub:
            result += 1
    return result

# Test the function
test_string = "aaa"
test_substring = "a"
result = how_many_times(test_string, test_substring)
assert result == 3

# Another test case
test_string = "hello"
test_substring = "ow"
result = how_many_times(test_string, test_substring)
assert result == 2
```