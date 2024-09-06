```python
def strlen(string: str) -> int:
    return len(string)

# Testing the function with valid inputs
test_strlen = str.test_strlen('')
# Should return 0
assert strlen(test_strlen) == 0

test_strlen = str.test_strlen('abc')
# Should return 3
assert strlen(test_strlen) == 3

# Testing the function with invalid input
test_bad_string = 'this is not a string'
# Should raise a ValueError
with pytest.assert expected=ValueError:
assert not strlen(test_bad_string)
```