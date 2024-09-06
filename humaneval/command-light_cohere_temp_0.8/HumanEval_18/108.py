```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string, 
    considering overlapping matches.
    Returns 0 if the isn't found anywhere, and raises an error if the substring is not found.
    """
    match(substring, string)
    return 1 + (not match)

# Test the function
test_string = "aaaaaaa"
test_substring = "a"
result = how_many_times(test_string, test_substring)
print(result) # Output: 3
```