Here's a Python script with a self-contained function that solves the problem:
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", " uvwxyzabcedefghijklmnopqr "))
```
The `encode_shift` function takes a string s and returns an encoded version of the string. For every character in the string, it adds 5 to the ASCII value, then takes the result modulo 26 to wrap around the alphabet. It then adds the difference between the wrap-around point and 'a' to get the encoded character, which it returns.

The `decode_shift` function takes a string s and returns a decoded version of the string. It uses the `translate` function with a `maketrans` style mapping to shift each character in the encoded string by 5 back to its original character. The mapping pairs each character of the encoded string with the character 5 places earlier in the alphabet. 

Both functions have self-contained logic to encode or decode a string and can be used independently without altering external state or requiring additional functions.