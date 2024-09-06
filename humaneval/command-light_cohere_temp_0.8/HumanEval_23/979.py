```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
assertEqual(strlen(''), 0)
assertEqual(strlen('')), 0, 'Empty string should have length 0')
assertEqual(strlen('abc'), 3)
assertEqual(strlen('abcde'), 6)
assertEqual(strlen('   abc   '), 5)
assertEqual(strlen('        '), 5)
assertEqual(strlen(' Vickers'), 13)
```
The provided Python script defines a function `strlen` that calculates the length of a given string. It then tests the different inputs and ensures the function's correctness through various assertions.