```python
def strlen(string: str) -> int:
    return len(string)

# Test case for empty string
assert strlen('') == 0

# Test case for only alphabetical characters
string = 'abc'
assert strlen(string) == 3

# Test case with spaces and special characters
string = '  hello#world!'
assert strlen(string) == 7

# Test case with empty string containing non-alphphanumeric characters
string = ''
assert strlen(string) == 0
```