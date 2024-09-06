```python
def string_xor(a: str, b: str) -> str:
    return bin(int(a, 2) ^ int(b, 2))[2:]
```
The provided Python script solves the problem by converting both input strings `a` and `b` to binary numbers using the `int(a, 2)` function, performing an XOR operation on these binary values, and then converting the result back to a string format. The `bin()` function is used to convert the binary XOR value to a string representation, while `[2:]` is used to remove the leading `'0b'` prefix. This approach ensures that the function correctly performs binary XOR on the input strings and returns the result as a string.