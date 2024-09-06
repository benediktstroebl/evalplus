```python
def strlen(string: str) -> int:
    return len(string)

# Test case for empty string
assertEqual(strlen(''), 0)

# Test case for one-character string
assertEqual(strlen('a'), 1)

# Test case for multiple characters string
assertEqual(strlen('abc'), 3)
```
This script defines a function `strlen` that calculates and returns the length of the given string. You can use this string length is often used to quickly determine if a string is empty, has only one character, or contains multiple characters. The solution is straightforward and complete in one line, making it easy to understand and maintain.