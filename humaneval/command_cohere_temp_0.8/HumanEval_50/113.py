```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) for ch in s])
```

This script defines two functions:
- `encode_shift` : Encodes the input string `s` by shifting every character by 5 in the alphabet.
- `decode_shift` : Decodes the input string `s` which was encoded using the `encode_shift` function. 

The functions apply the specified shift encoding/decoding to each character in the input string `s`. The final encoded or decoded string is returned as a concatenation of the transformed characters. 

This solution is applicable for encoding and decoding operations utilizing a 5-shift pattern in the alphabet for the input string. Feel free to customize the base alphabet letter and shift factors according to your specific requirements.