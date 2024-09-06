Here's a Python script with a self-contained function that solves the problem:
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "uskbnjmialpdwxyz"))
```
The `encode_shift` function takes a string s as input and returns an encoded version of the string. For every character in the string, it applies a shift of 5 in the alphabet. If the shifted character is larger than z, it wraps around the alphabet by taking modulo 26. The `decode_shift` function takes an encoded string s as input and returns the decoded string by undoing the shift on every character. It accomplishes this by creating a translation table with the string "abcdefghijklmnopqrstuvwxyz" shifted 5 places ahead in the alphabet as the from_stop, and the original alphabet as the to_stop. This ensures every character is shifted back by 5.