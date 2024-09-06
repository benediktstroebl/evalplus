Here's a Python script with a self-contained function that solves the problem:
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s.translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"))
```

The `encode_shift` function takes a string `s` as input and returns an encoded version of the string. For each character in the input string, it applies a simple formula to encode it by shifting each character by 5 in the alphabet. The modulus 26 ensures that the encoding wraps around to the beginning of the alphabet if necessary. The `decode_shift` function takes a string encoded with `encode_shift` function and returns the original decoded string. It uses the `translate` method to replace each encoded character with its corresponding decoded character.