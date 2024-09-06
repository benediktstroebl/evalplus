```python
def flip_case(string: str) -> str:
    return string.swap()
```

# Test case 1:
assert flip_case('hello') == 'olleH'

# Test case 2:
assert flip_case('HELLO') == 'olleO'

# Testcase 3:
assert flip_case('Hello world') == 'dlrow veol'

# Testcase 4:
assert flip_case('FOO Bar BAZ') == 'bAR zUBaZ BFFO'

# Testcase 5:
assert flip_case('hello world') == 'dlroW olleho'
```