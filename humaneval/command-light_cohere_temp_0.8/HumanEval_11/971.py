Here is a self-contained Python function that solves the problem of XORing two strings: 
```python
def string_xor(a: str, b: str) -> str:
    """ Returns the XOR of two input strings.

    a = [a[i] ^ b[i] for all i from 0 to len(a) - 1]
    return ''.join(a ^ b)
```

This function performs a bitwise XOR operation on the two input strings and returns the result as a single string. It uses the array operator `^^ to perform the XOR operation for each character in the strings.