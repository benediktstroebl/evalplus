```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) for ch in s])
```

This code defines two functions: `encode_shift` and `decode_shift`. 

`encode_shift` takes a string `s` as input and returns the encoded version of that string. It shifts each character in the string by 5 in the alphabet. Characters that would exceed the `ABCDEFGHIJKLMNOPQRSTUVWXYZ` range are wrapped around with the modulus operator `% 26`. The resulting encoded character is then converted back to a string and joined together with `join()` to form a string.

`decode_shift` takes a string `s` as input and returns the original string decoded from the encoding scheme used in `encode_shift`. It shifts each character in the string back by 5 in the alphabet. Similar to the encoding process, the decoding process also wraps around characters that exceed the `ABCDEFGHIJKLMNOPQRSTUVWXYZ` range with the modulus operator `% 26`. The resulting decoded character is then converted back to a string and joined together with `join()` to form a string. 

Overall, this script provides a way to encode a string by shifting each character by 5 in the alphabet and decode it back, allowing for the transformation between encoded and original strings.