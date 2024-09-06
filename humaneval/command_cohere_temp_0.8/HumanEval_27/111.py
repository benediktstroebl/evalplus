```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a new string where all lowercase characters are flipped to uppercase and all uppercase characters are flipped to lowercase. This is achieved by using a list comprehension that checks if each character is alphabetic using the `isalpha()` string method, and if so, uses the `swapcase()` method to flip the case. Non-alphabetic characters are left unchanged.

To test this function, you can run the following code:
```python
test_str = 'Hello, World!'
expected_result = 'hELLO, wORLD!'

assert flip_case(test_str) == expected_result
```

This will ensure that the function behaves as expected and produces the desired result when provided with a string.