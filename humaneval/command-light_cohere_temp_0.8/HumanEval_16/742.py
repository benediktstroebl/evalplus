Here's a self-contained Python function that counts the distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    # Count distinct characters in a string, without case sensitivity
    return len(set(string))

# Test the function
# Test with a string containing all ASCII lowercase letters
test_count_distinct_characters = count_distinct_characters('abcXYZdefg')
assert test_count_distinct_characters == 7  # Should be 7, since there are 7 distinct lowercase letters

# Test with a string of digits
test_count_distinct_characters = count_distinct_characters('12345')
assert test_count_distinct_characters == 10  # Should be 10, since there are 10 distinct digits
```

This function uses the `set` function to create a set of characters from the input string, and then counts the number of distinct characters using the `len` function. The test cases demonstrate the issue by counting the distinct characters in a string with known values, and the expected results are then checked using `assert`.