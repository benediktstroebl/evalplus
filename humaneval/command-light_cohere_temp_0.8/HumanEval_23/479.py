```python
def strlen(string: str) -> int:
    return len(string)

# Tests
assertEqual(strlen(''), 0)
assertEqual(strlen('abc')), 3)
assertEqual(strlen('   123456   ')), 12)
assertEqual(strlen(''), None)
assertEqual(strlen(__hello__)), 4)
```