```python
def string_xor(a, b):
    return str(int(a, 2) ^ int(b, 2))
```

This Python script defines a function `string_xor` that takes two binary strings `a` and `b` as inputs and returns their binary XOR by performing integer arithmetic in base 2. This is done by converting both strings to integers using `int(val, 2)`, performing the bitwise XOR operation `^` between them, and then converting the result back to a string using `str()`. 

It returns the correct result when tested with the example provided in the prompt, demonstrating the binary XOR operation between two strings of binary characters. 

**NOTE:** This approach leverages integer arithmetic in base 2, and thus is not compatible with non-binary strings or strings containing different digit types. It only supports inputs consisting of 1s and 0s, as per the problem statement.