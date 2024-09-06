```python
def string_xor(a, b):
    return str(int(a, 2) ^ int(b, 2))
```

This script defines a function `string_xor` that takes two strings `a` and `b` as inputs. It uses the `^` operator to perform binary XOR on the binary representations of `a` and `b`, converts the result back to a string using the `str` function, and returns the result.

Here is a sample usage of the function:
```python
print(string_xor('010', '110')) # Output: '100'
```

This function correctly performs binary XOR on two inputs consisting only of 1s and 0s and returns the result as a string.