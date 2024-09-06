```python
def string_xor(a: str, b: str) -> str:
    return ''.join(chr(int(x) ^ int(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two strings `a` and `b` as binary inputs (consisting of 1s and 0s) and performs a binary XOR operation on them. It uses `zip` to iterate over corresponding digits of both strings, takes their binary XOR, and converts it back to a string using `chr`.

Here is a simpler solution:
```python
def string_xor(a, b):
    return ''.join(x ^ y for x, y in zip(a, b))
```

This solution does the same but is slightly more readable. It uses the `^` operator which has a higher priority than `for` and `zip`, so there's no need for parentheses. Also, it's unnecessary to use `join` with a string concatenation character ('^') since this will be the result of the XOR operation.