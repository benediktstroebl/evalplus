```python
def string_xor(a, b):
    return str(int(a, 2) ^ int(b, 2))
```

This script defines a function `string_xor` that takes two strings `a` and `b` as inputs. It uses the `^` operator to perform binary XOR on the underlying integers represented by the binary strings `a` and `b`. The result is then converted back to a string using the `str` function, as required by the problem description.

To run this code, you can execute it in your local Python environment. You can also copy and paste the code into a Python interpreter console. Once executed, it will run and display the result, or an error message if the input is incorrect.

This code solves the problem of performing binary XOR on two binary strings, as described in the original problem statement. Specifically, it performs the XOR operation on the binary representations of the two input strings and returns the binary representation of the resulting integer.