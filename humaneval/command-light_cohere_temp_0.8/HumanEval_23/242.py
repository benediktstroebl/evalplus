```python
def strlen(string: str) -> int:
    return len(string)

# Test case 1
assertEqual('', strlen(''))
assertEqual(strlen(''), 0)

# Test case 2
assertEqual('abc', strlen('abc'))
assertEqual(strlen(''), 3)

# Test case 3
s = "hello world"
assertEqual(strlen(s)), 6)
```