```python
def strlen(string: str) -> int:
    """
    Return the length of the given string.

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


# Test cases
assert strlen('') == 0
assert strlen('abc') == 3
assert strlen('hello world') == 11

# Run tests and print success message
if all([
    strlen('') == 0,
    strlen('abc') == 3,
    strlen('hello world') == 11,
]):
    print("All tests passed.")
else:
    print("Tests failed.")
```

This Python script defines a function `strlen()` that returns the length of a given string. It includes three test cases to verify the correctness of the function. The `assert` statements check if the function behaves as expected. If all tests pass, it prints "All tests passed." Otherwise, it prints "Tests failed."