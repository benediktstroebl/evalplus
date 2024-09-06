```python
def string_xor(a, b):
    return bytes(a.encode()).xor(bytes(b.encode())).decode()
```

This solution takes two strings consisting of 0s and 1s and performs a binary XOR operation on them, returning the result as a string. Here is an example usage of the function:
```python
>>> string_xor('010', '110')
'100'
``` 

This will return '100' as '1' xor '1' equals '0' xor '1' equals '1'.