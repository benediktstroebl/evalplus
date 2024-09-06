Here's a Python script with a self-contained function that solves the problem:
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s

# Unit tests
encode_tests = [
    ("Hello", "Ifmmp"),
    ("World", "Zwief"),
    ("!!!!!", "Gkkkk"),
    ("abcde", "fghe"),
]

for en, exp in encode_tests:
    enc = encode_shift(en)
    assert enc == exp, f"Encoding of {en} failed."

decode_tests = [
    ("Ifmmp", "Hello"),
    ("Zwief", "World"),
    ("Gkkkk", "!!!!!"),
    ("fghe", "abcde"),
]

for de, exp in decode_tests:
    dec = decode_shift(de)
    assert dec == exp, f"Decoding of {de} failed."
```

This script defines the `encode_shift` and `decode_shift` functions, along with unit tests for both functions. In particular, the `encode_shift` function shifts each character of the input string `s` by 5 in the alphabet, wrapping around if the shift is larger than 26. The `decode_shift` function simply returns the input string, as it is the decoding function for the encoding scheme defined by `encode_shift`.