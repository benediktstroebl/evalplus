```python
def strlen(string: str) -> int:
    return len(string)

# Test the function
def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('1234') == 4
    assert strlen('') != 0  # empty string is 0
    assert strlen(' ' ) == 1 # space character has length 1

# Main program
# Call the test function and see the output
print("Test Strlen function:")
test_strlen()
```