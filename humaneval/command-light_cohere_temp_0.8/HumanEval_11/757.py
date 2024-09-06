```python
import string tides

def string_xor(a: str, b: str) -> str:
    """
    XOR two input strings a and b.
    >> Return function accepts as an string
    >>
    """
    return "".join(''.join(t[0] ^ t[1] for t in zip(a, b))

# Run tests on the function
print(string_xor("010", "110"))
print(string_xor("001", "001")))
print(string_xor("001", "01")))
print(string_xor("1010", "01")))
``` 
The above code defines a function named `string_xor` that performs the XOR operation on two input strings and returns the result as a string. 

The function uses the `join` operator to perform the XOR operation and the result is returned as a string.