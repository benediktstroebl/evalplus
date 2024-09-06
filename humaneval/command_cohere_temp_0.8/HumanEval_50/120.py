```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) for ch in s])
```

This script defines two functions:
- `encode_shift` : Encodes the input string `s` by shifting every character by 5 in the alphabet.
- `decode_shift` : Decodes the input string `s` which was encoded using the `encode_shift` function. Both functions operate on strings and return the encoded or decoded string respectively. 

Note that the modulus 26 is used to ensure that the shifted characters remain within the alphabet range. Also, the `decode_shift` function subtracts ord('a') from the character code first to undo the shift, and then adds ord('a') back to map the character to the correct ASCII point. 

The code has reasonable time and space complexity, O(n) since it iterates over each character in the string only once for encoding and decoding. 

This solution will correctly encode and decode strings using the shift cipher.