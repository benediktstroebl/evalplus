```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) for ch in s])
```

This script defines two functions:
- `encode_shift` : Encodes a string by shifting each character by 5 in the alphabet.
- `decode_shift` : Decodes an encoded string by shifting each character back by 5 in the alphabet. 

The functions are designed to work independently, and the output of `encode_shift` is suitable as input for `decode_shift`. 

Note that the functions assume that the input `str` contains only a-z characters. Characters that are not in this set are not affected by the 5-shift and will remain unchanged. If this behavior is not desired, you may need to implement additional checks and adjustments.