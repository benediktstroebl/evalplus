Here's a Python script with a self-contained function that solves the problem you've outlined, along with a markdown code block demonstrating how to use the function:
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "ijklmnopqrstuvwxyzabcdefgh"))
```
The functions encode_shift and decode_shift are defined to perform the relevant encoding or decoding operations. You can test these functions with suitable input strings to verify their behavior.

The enclosed code block demonstrates how to utilize these functions to encode and then decode a simple message:
```
```python
message = "Hello, World!"
encoded = encode_shift(message)
decoded = decode_shift(encoded)
print("Original:", message)
print("Encoded:", encoded)
print("Decoded:", decoded)
```
```
To use these functions, include the Python script in your project or copy the code into a suitable module. These functions can be called to encode or decode strings according to the alphabet shift scheme.  Please note that the specific solution relies on the Python 3 character mapping and translation methods.