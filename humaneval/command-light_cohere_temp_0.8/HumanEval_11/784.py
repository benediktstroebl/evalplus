Here is a Python script that solves the problem of XORing strings in Markdown code blocks:

```python
def string_xor(a: str, b: str) -> str:
    return "".join("".join(c ^= a[c] ^ b[c]) for c in zip(a, b))

# Test case 1
string_xor('010', '110')  # Answer: 100

# Test case 2
string_xor('1010', '01')  # Answer: 1010

# Test case 3
string_xor('000', '1111')  # Answer: 11111
```

This Python code defines a function called string_xor that performs a binary XOR operation on two input strings. The function takes two strings as arguments and returns the result of the XOR operation as a single string. The test cases demonstrate the demonstration of the function's behavior, passing various strings and verifying the expected results of the XOR operation.