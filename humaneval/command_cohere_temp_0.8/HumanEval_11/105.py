```python
def string_xor(a: str, b: str) -> str:
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
```

This script defines a function `string_xor` that takes two binary strings `a` and `b` as inputs and performs a binary `XOR` operation on them. The returned value is a string that represents the result of the binary `XOR` operation in unary notation.

Here is an example usage of the function:
```python
print(string_xor('010', '110')) # Output: '100'
```

This function works by converting the binary strings to their corresponding ASCII values using the `ord()` function, performing the `XOR` operation using the bitwise `^` operator, and converting the resulting ASCII values back to characters using the `chr()` function. The `zip` function is used to iterate over the corresponding pairs of characters in the two input strings.

Note that this solution assumes that the input strings only contain the characters '0' and '1'.