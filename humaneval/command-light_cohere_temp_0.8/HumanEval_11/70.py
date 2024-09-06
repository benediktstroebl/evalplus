Here's the self-contained Python function that solves the problem:
```python
def string_xor(a: str, b: str) -> str:
    return ''.join(c^=>(ord(a[i]) ^ ord(b[i])) for i, c in enumerate(a + b))
```
This function performs a binary XOR operation on two input strings, consisting only of digits represented by single digits (0 or 1). It uses the `enumer()` function in Python to iterate over each character in the input strings and performs the XOR operation using the `^=>(ord(a[i]) ^ ord(b[i]))` expression. The result is the string with the XOR operation applied.