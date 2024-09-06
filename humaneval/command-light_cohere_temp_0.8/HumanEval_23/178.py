```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
assertEqual(strlen(''), 0)
assertEqual(strlen('')), 0, msg="Empty string should have length 0")
assertEqual(strlen('abc'), 3)
assertEqual(strlen('hello world'), 13)
assertEqual(strlen('        '), 8)

# Example usage
print(strlen('abc'))
```