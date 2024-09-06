```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
assertEqual(strlen(''), 0)
assertEqual(strlen(' '), 1)
assertEqual(strlen('abc'), 3)
assertEqual(strlen('olu'), 5)

# Example usage
print(strlen('hello'))
```