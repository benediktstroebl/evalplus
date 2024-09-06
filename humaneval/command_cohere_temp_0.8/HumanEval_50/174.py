```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "ardtsuwopbfjkhemqyz"))
```

The `encode_shift` function shifts every character in the given string by 5 in the alphabet to obtain an encoded string. The `decode_shift` function reverses the encoding process to decode the string. This solution utilizes the `translate` method to decode the encoded string, based on the provided translation table. This method provides a more efficient solution than iterating over each character.