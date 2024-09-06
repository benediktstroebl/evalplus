```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, without overlapping.
    >>> string = 'aaaaaaa'
    sub = 'a'
    result = 0
    i = 0
    while i < len(string):
        if string[i] == sub:
            result += 1
        i += 1
    return result

# Test the function
test_string = 'aaaaaaa'a'
test_substring = 'a'
result = how_many_times(test_string, test_substring)
assert result == 3
```