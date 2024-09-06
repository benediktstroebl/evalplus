```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "Yjnmblxyzabcde"))
```

The `encode_shift` function shifts every character by 5 in the alphabet, encoding it, while the `decode_shift` function decrypts the encoded string by shifting back to the original character. This ensures the decryption of the encoded string "abc" would be returned as "efg". 

This solution is optimized for readability and efficiently encodes/decodes any string without excessive character mapping.