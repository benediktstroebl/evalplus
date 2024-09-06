```python
def string_xor(a: str, b: str) -> str:
    return bin(int(a, 2) ^ int(b, 2))[2:]
```
The provided code defines a function `string_xor` that takes two strings `a` and `b` consisting only of binary digits '0' and '1'. It employs the `int` function to convert these strings into binary integers, performs an XOR operation on these integers, and then converts the result back to a binary string using `bin`. The returned string only contains the two binary digits '0' and '1', thus ensuring that the result is also a valid binary string. 

Here is an example usage of the function providing an input and showing the operation's result:
```python
print(string_xor('010', '110'))  # Expected output: '100'
```
This method is computationally efficient and provides a clear and concise solution to the problem.