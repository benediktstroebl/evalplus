```python
def decode_shift(s: str):
    """
    Decodes a string encoded with encode_shift function.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
```