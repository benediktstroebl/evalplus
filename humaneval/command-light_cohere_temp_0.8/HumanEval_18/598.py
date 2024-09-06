```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string.
    >>> how_many_times('abcde', 'de')
    3
    """
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count

# Test cases
test_string = """abcde"` * 'abcbe'
test_substring = "de"
test_result = how_many_times(test_string, test_substring)
print(test_result)  # Output: 3
```