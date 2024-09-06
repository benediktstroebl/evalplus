```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr(((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) + ord("a")) for ch in s])
```

This script defines two functions:
1. `encode_shift`(): This function takes a string `s` as input and encodes it by shifting each character by 5 in the alphabet. It returns the encoded string.
2. `decode_shift`(): This function takes an encoded string `s` as input and returns the original decoded string. It corrects the encoding that was applied in the `encode_shift` function. 

The encoding and decoding processes ensure that the alphabet shift is maintained consistently, and it is corrected appropriately for decoding.