```python
def string_xor(a: str, b: str) -> str:
    return bin(int(a, 2) ^ int(b, 2))[2:]
```
The provided Python script defines a function `string_xor` that performs binary XOR on two input strings `a` and `b`, which consist only of characters '0' and '1'. It converts these strings to binary numbers, performs the XOR operation bitwise, and converts the result back to a string. 

Here is an example usage of the function:
```python
>>> string_xor('010', '110')
'100'
```

This method has a time complexity of O(log(min(a, b))). The resulting string will contain zeros and ones, representing the binary XOR of the two input strings.