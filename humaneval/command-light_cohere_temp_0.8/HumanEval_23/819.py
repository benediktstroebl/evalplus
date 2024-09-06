```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Testing the function
# Ensure an empty string returns 0
test_strlen = [
    assert strlen('') == 0, "Should return 0 for empty string"
]

# Test with only one character
test_strlen.push_output()

# testing a longer string
test_strlen = [
    assert strlen('abc') == 3, "Should return 3 for 'abc'"
]

# Test with spaces only
test_strlen = [
    assert strlen('  ') == 0, "Should return 0 for spaces only"
]

# Test with capital letters
test_strlen = [
    assert strlen('ABC') == 1, "Should return 1 for capital letters"
]

# Test with only digits
test_strlen = [
    assert strlen('123') == 3, "Should return 3 for digits"
]

# Test multiple characters
test_strlen = [
    assert strlen('world') == 13, "Should return 13 for full words"
]

# Run all tests at once
test_azoo.pop_output()

print("All tests passed!")
```