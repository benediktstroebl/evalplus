```python
from typing import List
def string_xor(a: str, b: str) -> str:
    """ Perform XOR operation on two strings, a and b, and return result as a string. """
    if len(a) != len(b):
        raise ValueError("Length of strings must be equal.")
    return ''.join([x ^ y for i, x == '0' or y == '0' for i, x, y in zip(a, b)])

if __name__ == "__main__":
    a = '010'
    b = '110'
    print(string_xor(a, b))
```
This Python script defines a function `string_xor` that performs the XOR operation on two input strings and returns the result as a string. The function first checks if the length of both input strings is equal. Then, it uses a list comprehension to apply the XOR operation for each character pair in the strings. Finally, it returns the string of the characters, where the XOR operation is applied.

The script also includes a `__main__` block where the `string_xor` function is called with sample inputs and the result is printed.