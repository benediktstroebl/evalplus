```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", " abcdefghijklmnopqrstuvwxyz"))
```
The `decode_shift` function uses the `translate` method to shift each character back to its original position in the alphabet. The `maketrans` function creates a translation table that maps each shifted character to its original position. This approach is more efficient and avoids the character-by-character iteration used in the original prompt.