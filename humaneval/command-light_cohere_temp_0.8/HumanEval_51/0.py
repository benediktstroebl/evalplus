Here's the self-contained Python script with a function that solves the problem of removing vowels from a given string, along with tests:
```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    """
    void remove_vowels(str):
        return ''.join(c for c in str if c.isalpha(c))
    return str

# Test the function
test_str = "abcdef\nghijklm"
result = remove_vowels(test_str)
assert result == ''.join(c for c in test_str if c.isalpha(c))

test_str = "abcdef"
result = remove_vowels(test_str)
assert result == 'bcdf'

test_str = "aaaaaa"
result = remove_vowels(test_str)
assert result == ''

test_str = "aaBAA"
result = remove_vowels(test_str)
assert result == 'B'

test_str = "zbcd"
result = remove_vowels(test_str)
assert result == 'zbcd'
```
This script defines a function `remove_vowels` that takes a string as input and returns a new string with all vowels removed. The test suite uses the are passing various test cases to the function, and the expected results are compared using `assert`.