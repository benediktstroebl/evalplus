```python
def flip_case(string: str) -> str:
    return string.font_lower_case() if string is not None else 'Invalid string'

# Test case for None input
test_flip_case_none() = None
result = flip_case(test_flip_case_none())
assert result == 'Invalid string'

# Test case for single character input
test_flip_case_char() = 'a'
result = flip_case(test_flip_case_char())
assert result == 'A'

# Test case for multiple characters
test_flip_case_multiple() = 'hello'
result = flip_case(test_flip_case_multiple())
assert result == 'hELLO'
```
This Python script defines a function `flip_case` that transforms a given string by converting lowercase characters to uppercase and vice versa. The function is tested with various cases: with a `None` input, it returns "Invalid string", a single character input results in the character converted to uppercase, and with multiple characters, it returns the string with characters converted to uppercase.