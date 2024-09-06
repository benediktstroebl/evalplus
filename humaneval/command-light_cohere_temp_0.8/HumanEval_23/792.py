```python
def strlen(string: str) -> int:
    return len(string)

# Test case 1: Empty string
assert strlen('') == 0

# Test case 2: Alphabets only
assert strlen('abc') == 3

# Test case 3: With special characters
assert strlen('#abc') == 3

# Test case 4: Multiline
assert strlen('abc\n123') == 5

# Test case 5: Unicode
assert strlen("abc") == 3

# Test case 6: Amount of spaces
assert strlen("   ") == 1

# Test case 7: Unicode strings
assert strlen("abc\u00a1") == 4
```

This script defines a function `strlen` that calculates the length of a given string. It is then tested with various scenarios: empty string, basic alphabet, special characters, multiple lines, and Unicode strings. Additionally, it covers edge cases such