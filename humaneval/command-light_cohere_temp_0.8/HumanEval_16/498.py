```python
def count_distinct_characters(string: str):
    return len({c for c in string.string() if c not in string. characters()})
unique characters.

# Test cases
test_distinct_characters('xyzXYZ')  # Output: 3
test_distinct_characters('jerry')  # Output: 4
test_distinct_characters(' 1234 )  # Output: 4
test_distinct_characters('  ')  # Output: 4
```

This function utilizes a set to automatically filter and count unique characters in the input string. It's an concise and efficient approach that does not rely on a built-in function.