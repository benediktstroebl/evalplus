```python
def strlen(string: str) -> int:
    return len(string)

# Tests
assertEqual(strlen(''), 0)
assertEqual(strlen('')), 0, msg="Empty string"
assertEqual(strlen('abc')), 3, msg="Single character"
assertEqual(strlen('abcabc'), 3, msg="Double characters")
```