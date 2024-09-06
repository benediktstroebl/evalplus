Here is a self-contained Python function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

#Test cases
assertEqual(strlen(''), 0)
assertEqual(strlen('abc'), 3)
assertEqual(strlen('abcde'), 6)
assertEqual(strlen(''), 0)  # empty string is 0
```
The `assertEqual` function is used for unit tests, which checks that the function `strlen` returns the correct results for different inputs.