Here is a self-contained Python script that solves the problem of finding the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
assertEqual(strlen(''),            0)
assertEqual(strlen('')),        0
assertEqual(strlen('abc')),    3
assertEqual(strlen('aaaa')),   6
assertEqual(strlen('abcde')), 5

# Example usage
print(strlen('abcde'))
```

In this code, the `strlen` function takes a string as an argument and returns its length using the built-in `len()` function. The test cases ensure that the function works correctly for different inputs, and the `assertEqual` function is used to verify the correctness of the function.